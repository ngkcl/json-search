<template>
    <div clas="search-and-results-wrapper">
        <search-input 
            @searchResults="onSearchResults"
            @searchData="onRecieveSearchData"
        />
        <results-list 
            v-bind:resultsList="searchResults"
            @loadMore="loadMore"
        />
    </div>
</template>

<script>
import SearchInput from '../molecules/SearchInput';
import ResultsList from '../molecules/ResultsList';

import {
    searchPage
} from '../../utils/search'

export default {
    name: 'search-and-results',
    components: {
        SearchInput,
        ResultsList
    },
    data() {
        return {
            searchResults: null,
            currentPage: 2,
            searchedTerm: null
        }
    },
    methods: {
        onRecieveSearchData(searchData) {
            this.searchedTerm = searchData;
        },
        onSearchResults(results) {
            this.searchResults = results;
            this.currentPage = 2;
        },
        async loadMore() {
            let newResults = await searchPage(this.searchedTerm, this.currentPage)
            this.currentPage += 1;

            this.searchResults = [...this.searchResults, ...newResults]
        }
    }
}
</script>