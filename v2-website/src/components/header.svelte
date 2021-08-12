<header id="header">
    <a href="/" class="logo">
        <div>
            <h1 class="logo">UABiomed</h1>
            <span id="logo" class="image object">
                <img src="images/logo.jpg" alt="" />
            </span>
        </div>
    </a>
    <ul class="icons">
        {#each medias as media}
            <li>
                <a href={media.link} title={media.name} class='icon {media.icon}'>
            </li>
        {/each}
    </ul>
</header>

<script>
    const medias = [
        {name: 'Newsletter Subscription', link: 'http://eepurl.com/hjH5uf', icon: 'fa-envelope-square'},
        {name: 'Facebook', link: 'https://www.facebook.com/UAlbertaBiomed', icon: 'fa-facebook' },
        {name: 'Instagram', link: 'https://www.instagram.com/uabiomedclub/', icon: 'fa-instagram' },
        {name: 'Linkedin', link: 'https://ca.linkedin.com/company/uabiomed', icon: 'fa-linkedin' },
    ]
</script>

<style>
    div {
        display: flex;
        align-items: center;
    }
    .image img {
        height: auto;
        width: 60px;
    }
</style>
