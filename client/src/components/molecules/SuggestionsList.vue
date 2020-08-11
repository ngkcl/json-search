<template>
    <ul 
        class="suggestions-list" 
        style="list-style-type:none;"
        v-if="suggestions"
    >
        <li 
            v-for="(suggestion, i) in suggestions"
            :key="i"
            class="suggestion"
            @click="$emit('update:suggestion', suggestion)"
        >
            {{suggestion}}
        </li>
    </ul>
</template>

<script>

export default {
    name: 'suggestions-list',
    props: {
        suggestions: {
            type: Array,
            default: null
        }
    }
}
</script>

<style scoped>
.suggestions-list {
    width: 200px;
    padding-left: 10px;
    background: #fff;
    border: 1px solid black;
}

.suggestion {
    display:flex;
    padding-right:2em;
}
    
.suggestion:hover, .suggestion a:hover{
    background:#ddd;
    color:#777;
}
</style>