<header id="header">
    <a href="/" class="logo">UAlberta <strong>Biomed</strong></a>
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
        {name: 'Facebook', link: 'https://www.facebook.com/UAlbertaBiomed', icon: 'fa-facebook' },
        {name: 'Instagram', link: 'https://www.instagram.com/uabiomed/', icon: 'fa-instagram' },
        {name: 'Linkedin', link: 'https://ca.linkedin.com/company/uabiomed', icon: 'fa-linkedin' },
    ]
</script>

