<template>
    <div class="results-list-wrapper">
        <ul 
            style="list-style-type:none;"
            v-infinite-scroll="loadMore"
        >
            <result 
                v-for="result in resultsList" 
                :key="result.postcode" 
                v-bind:result="result"
            />
            <p
                v-if="Array.isArray(resultsList) && resultsList.length <= 0"
            >
                No results...
            </p>
            <p
                v-if="!resultsList"
            >
                Please search in the box above
            </p>
        </ul>
    </div>
</template>


<script>
import Result from './Result';

export default {
    name: 'results-list',
    props: {
        resultsList: Array
    },
    components: {
        Result,
    },
    methods: {
        loadMore() {
            if (this.resultsList) {
                console.log('load more called from ResultsList')
                this.$emit('loadMore')
            }
        }
    }
}
</script>