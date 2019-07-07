<section>
    <h2>Related Press</h2>
    {#each news as n}
        <News {...n} />
    {/each}
</section>

<script>
    import News from '../components/newsStory.svelte'

    const news = [
        {
            link: 'https://www.ualberta.ca/science/science-news/2019/march/exoskeleton-student-group-biomed',
            source: 'Ualberta',
            blurb: 'On March 4, 2019, UA Biomed had the opportunity to interview with the University of Alberta’s,Faculty of Science department to bring awareness to the group and the opportunities for undergraduate science students to join and contribute to the project. Clayton Molter and Ben Hallworth talked to the Faculty regarding the diverse opportunities that the group offers and the project specifically, being the industrial exoskeleton.'
        },
        {
            link: 'https://edmontonjournal.com/news/local-news/bionic-strength-u-of-a-students-designing-upper-body-exoskeleton-to-assist-labourers',
            source: 'Edmonton Journal',
            blurb: 'On March 6, 2019, UA Biomed had the opportunity to interview with the Edmonton Journal regarding their design for the industrial exoskeleton. Ben Hallworth talked aboutthe purpose of the exosuit and the targeted competition that the suit is being designed for.'
        },
        {
            link: 'https://www.cbc.ca/news/canada/edmonton/exoskeleton-prototype-provide-strength-for-workers-university-of-alberta-1.5043774',
            source: 'CBC News',
            blurb: 'On March 5, 2019, UA Biomedhad the opportunity to interview with CBC Edmonton regarding the exosuit design and purpose as well. Ben Hallworth discussed existing exoskeleton systems that are on the market and in use at big company facilities such as Ford and GM. He also outlined how the UA Biomed suit is different from these existing designs and what the plans are for the suit.'
        }
    ]
</script>
