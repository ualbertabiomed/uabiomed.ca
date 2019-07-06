<svelte:head>
	<title>UAB</title>
</svelte:head>

<div>
    <div id="wrapper">
        <div id="main" on:click={hideSideBar}>
            <div class="inner">
                <Header />
                <slot><!-- Pages go in here --></slot>
            </div>
        </div>

        <Sidebar />

    </div>
</div>

<script>
    import Sidebar  from '../components/sidebar.svelte'
    import Header from '../components/header.svelte'

    import { isSidebarEnabled } from '../stores/app.js'

    const hideSideBar = (event) => isSidebarEnabled.set(false)

</script>
