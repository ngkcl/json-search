<template>
    <div class="input-field-wrapper">
        <input 
            type="text" 
            v-model="inputData"
            @keyup="
                $emit('update:inputData', inputData);
                debounce()
            "
        />
    </div>
</template>

<script>
import _ from 'lodash';

export default {
    name: 'input-field',
    data() {
        return {
            inputData: ""
        }
    },
    props: {
        clickedSuggestion: {
            type: String,
            default: null,
            require: false
        }
    },
    methods: {
        debounce: _.debounce(function () {
            console.log('debouncing in input')
            this.$emit('debounce')
        }, 100)
    },
    watch: {
        clickedSuggestion: function(newVal) {
            console.log('Prop changed ', newVal)
            this.inputData = newVal;
        }
    }
}
</script>