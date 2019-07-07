<div>
    <h3> {title} </h3>
    <p> {blurb} </p>
    <div class='row'>
        {#each members as member}
            <Member {...member}/>
        {/each}
    </div>
    <hr class='major'/>
</div>

<script>
    import Member from './member.svelte'

    export let title
    export let blurb
    export let members
</script>
