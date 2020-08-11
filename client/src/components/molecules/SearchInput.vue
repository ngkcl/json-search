<template>
    <div class="search-input-wrapper">
        <div class="input-and-suggestions">
            <input-field
                class="search-input-field"
                @update:inputData="onChange"
                @debounce="onDebounce"
                :clickedSuggestion="clickedSuggestion"
            />
            <suggestions-list 
                class="suggestions-list"
                :suggestions="suggestions"
                @update:suggestion="onSuggestionClick"
            />
        </div>
        <action-button
            class="search-input-button"
            @click="onSubmit"
        >
            Search
        </action-button>
    </div>
</template>

<script>
import ActionButton from '../atoms/ActionButton';
import InputField from '../atoms/InputField';
import SuggestionsList from './SuggestionsList';

import {
    // search,
    suggest,
    searchPage
} from '../../utils/search';

export default {
    name: 'search-input',
    components: {
        InputField,
        ActionButton,
        SuggestionsList
    },
    data() {
        return {
            searchData: "",
            suggestions: null,
            clickedSuggestion: null
        }
    },
    methods: {
        async onSubmit() {
            this.suggestions = null;

            let searchResults = await searchPage(this.searchData, 1);
            console.log(searchResults)

            this.$emit('searchResults', searchResults)
            this.$emit('searchData', this.searchData)

        },
        onChange(newData) {
            this.searchData = newData;
            if (this.searchData == "") {
                this.suggestions = null;
            }
        },
        async onDebounce() {
            let newSuggestions = await suggest(this.searchData)
            this.suggestions = newSuggestions;
        },
        onSuggestionClick(suggestion) {
            this.clickedSuggestion = suggestion;
            this.suggestions = null;
        }
    },
}
</script>

<style scoped>
.search-input-wrapper {
    display: flex;
    flex-direction: row;
    width: 100%;
    justify-content: center;
}

.search-input-button {
    border-radius: 7px;
    height: 50
}

.input-and-suggestions {
    display: flex;
    flex-direction: column;
    width: 200px;
    margin-right: 25px;
}

.suggestions-list {
    flex-flow: column;
    position: absolute;
    margin-top: 40px;
}
</style>