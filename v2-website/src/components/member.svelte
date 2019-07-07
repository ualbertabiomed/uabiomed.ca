<div class='box person-box col-6 col-12-medium'>
    <div>
        <p><b>{name}</b></p>
        <p>{role}</p>
        <p>{year}</p>
    </div>
    <Avatar {src} {name} />
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
</style>

<script>
    import Avatar from './avatar.svelte'
    export let name
    export let src
    export let year
    export let role
</script>
