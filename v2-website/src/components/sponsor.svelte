<div class='box person-box col-6 col-12-medium'>
    <div>
        <p><b>{name}</b></p>
        <p>{role}</p>
    </div>
    <div class="image">
        <img src={src} />
    </div>
</div>

<style>
    .person-box {
        display: flex;
        align-items: center;
        justify-content: space-around;
    }

    p {
        margin: 0;
    }

    .image {
    }
</style>

<script>
    export let name
    export let src
    export let role
</script>
