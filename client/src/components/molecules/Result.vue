<template>
    <li>
        <div class="result">
            <div class="result-header">
                <p> {{result.name}} </p>
            </div>
            <div class="result-content">
                <p>Postcode:</p>
                <p>{{result.postcode}}</p>
            </div>
        </div>
    </li>
</template>

<script>
export default {
    name: 'result',
    props: {
        result: {
            name: {
                type: String,
                required: true
            },
            postcode: {
                type: String,
                required: true
            }
        }
    }
}
</script>

<style scoped>
.result {
    display: flex;
    flex-direction: column;
    border: 1px black solid;
    margin: 40px;
}
.result-header {
    height: 30%;
    background: gray;
    color: white;
    text-align: center;
}
.result-content {
    padding: 2px 16px;
}


</style>