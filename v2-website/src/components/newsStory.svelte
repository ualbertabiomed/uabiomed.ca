<div class="news">
    <h3>{source}</h3>
    <p>{blurb}</p>
    <a href={link}>Read more here</a>
    <hr class='major' />
</div>

<style>
    .news {
        width: 80%;
        margin-left: 10%;
        margin-top: 50px;
    }
    p {
        margin-bottom: 0;
    }
</style>


<script>
    export let blurb
    export let link
    export let source
</script>
