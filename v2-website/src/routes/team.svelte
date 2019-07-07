<section>
    <h2>The Team</h2>
    <div class='bound'>
        <span class='image fit'>
            <img src='images/Team.jpg' alt='Team Photo' />
        </span>
    </div>
    {#each teams as team}
        <Team {...team} />
    {/each}
</section>

<style>
    .bound {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .image.fit {
        max-width: 800px;
    }
</style>

<script>
    import Team from '../components/team.svelte'
    const teams = [
        {
            title: 'Control Team',
            blurb: 'The control team is working on designing the feedback system of the exoskeleton, as well as designing the system that allows the suit to give the user mechanical advantage.',
            members: [
                { name: 'Laura Petrich', src: 'images/people/Laura.jpg', role: 'Control team lead', year: '4th year Computer Science, Honors' },
                { name: 'Taylor Zowtuk', src: 'images/people/Taylor.jpg', role: 'Control team lead', year: '3rd year Computer Science, After Degree' }
            ]
        },
        {
            title: 'Biomechanics Team',
            blurb: 'The Biomechanics team is working on the structural design of the exoskeleton. They investigate human motion and work to build an ergonomic and effective suit that the Control team can bring to life.',
            members: [
                { name: 'Isobel Teteau', src: 'images/people/Isobel.jpg', role: 'Biomechanics team lead', year: '3rd Year Mechanical Engineering, Biomedical' },
                { name: 'Ahmed Abd El-Gelil', src: 'images/people/Ahmed.png', role: 'Biomechanics team lead', year: '2nd Year Mechanical Engineering, Biomedical' }
            ]
        },
        {
            title: 'Commercial Team',
            blurb: 'The commercial team is working on securing sponsorships for UAB.',
            members: [
                { name: 'Sunny Yang', src: 'images/people/Sunny.jpg', role: 'Commercial team Lead', year: '2nd Year Civil Engineering' }
            ]
        },
        {
            title: 'Executive Team',
            blurb: 'The executive team is working on making sure everything is going along smoothly, and nothing gets missed.',
            members: [
                { name: 'Ben Hallworth', src: 'images/people/Ben.jpg', role: 'President', year: '3rd Year Mechanical Engineering, Biomedical' },
                { name: 'Alicia MacDonald', src: 'images/people/Alicia.jpg', role: 'Project Manager', year: '3rd Year Mechanical Engineering, Biomedical' },
                { name: 'Aabid Wadood', src: 'images/people/Aabid.jpg', role: 'VP External', year: '2nd Year Mechanical Engineering, Biomedical' },
                { name: 'Qibang Feng', src: 'images/people/Qibang.jpg', role: 'VP Finance', year: '4th Year Finance Major, Economics Minor' }
            ]
        },
    ]
</script>
