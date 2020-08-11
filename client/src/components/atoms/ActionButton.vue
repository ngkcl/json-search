<template>
    <button :style="buttonStyles" @click="onClick">
        <slot>
        </slot>
    </button>
</template>


<script>
export default {
    name: 'action-button',
    data() {
        return {
            buttonStyles: {
                border: '1px solid #c9c9c9',
                borderRadius: 3,
                backgroundColor: '#c4c0c0',
                cursor: 'pointer',
                fontSize: 15,
                padding: '5px 20px',
                margin: 10,
            }
        }
    },
    methods: {
        onClick() {
            this.$emit('click');
        }
    }
}
</script>