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
    <h2> Team Testimonials </h2>
    <p>
        "UAB has been a great place to develop my creative design and project
        management skills. My team members were quick to show me the ropes
        regarding 3D modelling software before I learned it in class, as well
        as get involved in the design process. As someone who has a strong
        interest in anatomy and problem solving, I always look forward to
        meetings because I know I'll be learning something new!"

        <br>
            <b>– Femi, Current Biomechanics Team Member</b>
    </p>

    <p>
        "Working in the Controls team allows me to brainstorm, design, and
        implement an entirely new software project from the ground - up. Having
        my original thoughts and ideas be used in the beginning stages of the
        software development for the exoskeleton is the most exciting thing for
        me as a member in the Controls team. Working alongside the rest of the
        Controls team gives me an opportunity to work on a project amongst
        amazing and dedicated people."

        <br>
            <b>– Cyrus, current Control and Power Team Lead, former Control and Power Team Member</b>
    </p>

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
            title: 'Control and Power Team',
            blurb: 'The Control and Power team is working on designing the feedback system for the exoskeleton, as well as designing the system that allows the suit to give the user a mechanical advantage.',
            members: [
                { name: 'Laura Petrich', src: 'images/people/Laura.jpg', role: 'Control and Power Team Manager', year: '4th Year Computer Science, Honors' },
                { name: 'Taylor Zowtuk', src: 'images/people/Taylor.jpg', role: 'Control and Power Lead - Software', year: '3rd Year Computing Science, After Degree' },
                { name: 'Cyrus Diego', src: 'images/people/Cyrus.jpg', role: 'Control and Power Lead - Hardware', year: '3rd Year Computer Engineering, Software Specialization' },
                { name: 'Adil Younus', src: 'images/people/Adil.jpg', role: 'Control and Power Lead - Power', year: '2nd Year Electrical Engineering' },
                { name: 'Qiulin Yu', src: 'images/people/Qiulin.jpg', role: 'Control and Power Team Member', year: '3rd Year Mechanical Engineering' },
                { name: 'Jacob Reckhard', src: 'images/people/Jacob.jpg', role: 'Control and Power Team Member', year: '4th Year Mechanical Engineering' },
            ]
        },
        {
            title: 'Biomechanics Team',
            blurb: 'The Biomechanics team is working on the structural design of the exoskeleton. They investigate human motion and work to build an ergonomic and effective suit that the Control and Power team can bring to life.',
            members: [
                { name: 'Isobel Tetreau', src: 'images/people/Isobel.jpg', role: 'Biomechanics Team Manager', year: '4th Year Mechanical Engineering, Biomedical Specialization' },
                { name: 'Ahmed Abd El-Gelil', src: 'images/people/Ahmed.png', role: 'Biomechanics Team Lead', year: '3rd Year Mechanical Engineering, Biomedical Specialization' },
                { name: 'Xiao Meng', src: 'images/people/Xiao.jpg', role: 'Biomechanics Team Lead', year: '3rd Year Mechanical Engineering, Biomedical Specialization' },
                { name: 'Tully Underhill', src: 'images/people/Tully.jpg', role: 'Biomechanics Team Lead', year: '3rd Year Mechanical Engineering, Biomedical Specialization' },
                { name: 'Isaiah Wong', src: 'images/people/Isaiah.jpg', role: 'Biomechanics Team Member - Motor Mount Specialist', year: '3rd Year Mechanical Engineering' },
                { name: 'Kiernan Carroll', src: 'images/people/Kiernan.jpg', role: 'Biomechanics Team Member - Motor Mount Specialist', year: '3rd Year Mechanical Engineering' },
            ]
        },
        {
            title: 'Commercial Team',
            blurb: 'The Commercial team works on securing corporate sponsorships, assessing the marketability of the device, and budgeting for the teams prototyping.',
            members: [
                { name: 'Josh Lau', src: 'images/people/Josh.jpg', role: 'Commercial Team Lead', year: '4th year Mechanical Engineering' },
                { name: 'Victor Egruen-Echaiz', src: 'images/people/Victor.jpg', role: 'Commercial Team Lead', year: '3rd Year Business, Human Resources Major' },
                { name: 'Sunny Yang', src: 'images/people/Sunny.jpg', role: 'Commercial Team Member', year: '2nd Year Civil Engineering' },
            ]
        },
        {
            title: 'Executive Team',
            blurb: 'The executive team is working on making sure everything is going along smoothly, and nothing gets missed.',
            members: [
                { name: 'Ben Hallworth', src: 'images/people/Ben.jpg', role: 'President', year: '4th Year Mechanical Engineering, Biomedical Specialization' },
                { name: 'Alicia MacDonald', src: 'images/people/Alicia.jpg', role: 'Project Manager', year: '4th Year Mechanical Engineering, Biomedical Specialization' },
                { name: 'Aabid Wadood', src: 'images/people/Aabid.jpg', role: 'VP External', year: '3rd Year Mechanical Engineering, Biomedical Specialization' },
                { name: 'Qibang Feng', src: 'images/people/Qibang.jpg', role: 'VP Finance', year: '4th Year Finance Major, Economics Minor' },
            ]
        },
    ]
</script>
