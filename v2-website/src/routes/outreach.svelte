<section>
    {#each events as event}
        <Outreach {...event} />
    {/each}
</section>

<script>
    import Outreach from '../components/outreachEvent.svelte'

    const events = [
        {
            title: 'Windsor Park',
            date: 'June 21 2019',
            photos: ['images/outreach/windsor/1.jpg', 'images/outreach/windsor/2.jpg'],
            story: `
Today, UA Biomed had the opportunity to do an outreach presentation at the
Windsor Park Elementary School, to a lovely class of grade three students. The
students had endless questions regarding the capabilities of exoskeleton suits
and engineering in general. Alica and Aabid had fun talking about the
possibilities of flying and fireproof exoskeleton designs for a futuristic
world.
`
        },
        {
            title: 'DiscoverE',
            date: 'July 5th 2019',
            photos: ['images/outreach/discovere/1.jpg', 'images/outreach/discovere/2.jpg'],
            story: `
Today, UA Biomed had the opportunity to do an outreach presentation at the
DiscoverE camps to an energetic group of grade two and three kids. The kids
asked questions about chemical engineering, and the oil and gas industry. They
were also curious if our exosuit could be used for insects who lost their own
exoskeletons!
`
        }
    ]
</script>
