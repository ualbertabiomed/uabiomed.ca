<article class="page">
    <p class='title'><b>{title}</b>, {date}</p>
    <div>
        <p>
            {story}
        </p>
        <div class='image-box row gtr-50 gtr-uniform'>
            {#each photos as photo}
                <div class='col-6 col-12-medium'>
                    <span class='image fit'>
                        <img src={photo} alt='Photo of the outreach event'/>
                    </span>
                </div>
            {/each}
        </div>
    </div>
</article>

<style>
    .title {
        font-size: 2em;
        margin-bottom: 1em;
    }
    .image-box {
        margin-bottom: 6em;
    }
    .page {
        width: 80%;
        margin-left: 10%;
        margin-top: 50px;
    }
</style>


<script>
    export let title
    export let date
    export let photos
    export let story
</script>
