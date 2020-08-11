#!/usr/bin/env python3
# encoding: utf-8

from whoosh.index import create_in
from whoosh.fields import *

try:
     import config
except:
     import json_search.config as config

from pathlib import Path

import logging

from whoosh.qparser import MultifieldParser

'''
NOTE:

Since I wanted to make this work with even larger datasets, 
I decided to choose a faster JSON parser and came upon 
orjson which benchmarks as the fastest one for Python

There is a benchmark comparison in the tests
'''
import orjson

class Searcher():
     def __init__(self, index_data = config.INDEX_DIR, *args, **kwargs):
          # Default schema
          # TODO: Get from config. Cue maybe? Yaml?
          self.schema = Schema(name=NGRAM(stored=True), postcode=NGRAM(stored=True))
          
     def generate_index(self, index_dir = config.INDEX_DIR, index_data = config.DATA_FILE):
          """
          Generates a searchable index from the given json data
          """

          index_path = Path(index_dir)

          if not index_path.exists():
               index_path.mkdir(parents=True)


          # Create index
          self.ix = create_in(str(config.INDEX_DIR), self.schema)

          # Load data from json
          with open(index_data) as f:
               data = orjson.loads(f.read())

          # Write data to index
          with self.ix.writer() as writer:
               for item in data:
                    writer.add_document(name=str(item['name']),
                                        postcode=str(item['postcode']))

     # TODO: Return type
     def _generate_query_obj(self, text, fields = ["postcode", "name"]):
          """
          Parses query based on text.
          """
          if not self.ix:
               raise Exception("Index not created")

          query = MultifieldParser(fields, self.ix.schema).parse(text)
          return query

     def search(self, text) -> list:
          """
               Searches the index for a given term (text)
          """
          try:
               q = self._generate_query_obj(text)
          except Exception as _:
               # Propagate Exception
               raise
          
          # Get search results
          with self.ix.searcher() as searcher:
               search_res = searcher.search(q, terms=True)

               # one-liner to get results as a list of dicts
               results = [{
                    "name": hit['name'], 
                    "postcode": hit['postcode']
                } for hit in search_res]

               return results
     
     def search_page(self, text, page, page_len=3) -> list:
          """
               Searches the index by page and page length
          """
          try:
               q = self._generate_query_obj(text)
          except Exception as _:
               # Propagate Exception
               raise
          
          # Get search results
          with self.ix.searcher() as searcher:
               search_res = searcher.search_page(q, page, page_len, terms=True)

               # one-liner to get results as a list of dicts
               results = [{
                    "name": hit['name'], 
                    "postcode": hit['postcode']
                } for hit in search_res]

               return results
     
     def suggest(self, text) -> list:
          """
          Provides suggestions from index for a given string
          """
          with self.ix.reader() as r:
               postcode_suggestions = [i.decode('utf-8') for i in r.expand_prefix('postcode', text)]
               name_suggestions = [i.decode('utf-8') for i in r.expand_prefix('name', text)]

               # Concatenate arrays
               return [*postcode_suggestions, *name_suggestions]