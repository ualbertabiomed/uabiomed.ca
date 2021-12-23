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
                { name: 'Justin Boileau', src: 'images/people/Justin.jpg', role: 'Control and Power Team Lead - Software', year: '3rd Year Computer Engineering, Software Specialization' },
                { name: 'Daren Trin', src: 'images/people/Daren.jpg', role: 'Control and Power Team Lead - Electrical', year: '3rd Year Computer Science' },
                { name: 'Ryan Kortbeek', src: 'images/people/Ryan.jpg', role: 'Control and Power Team Member - Software', year: '4th Year Computer Engineering, Software Specialization' },
                { name: 'Preston Ling', src: 'images/people/Placeholder.jpg', role: 'Control and Power Team Member - Software', year: '3rd Year Computer Science'},
                { name: 'Ethan Lai', src: 'images/people/Placeholder.jpg', role: 'Control and Power Team Member - Electrical', year: '3rd Year Electrical Engineering'},
                { name: 'Keish Chandel', src: 'images/people/Placeholder.jpg', role: 'Control and Power Team Member - Electrical', year: '3rd Year Electrical Engineering' },
                { name: 'Gordon Ren', src: 'images/people/Placeholder.jpg', role: 'Control and Power Team Member - Electrical', year: '3rd Year Electrical Engineering' },
                { name: 'Alphonso Dineros', src: 'images/people/Placeholder.jpg', role: 'Control and Power Team Member - Software', year: '3rd Year Computer Engineering, Software Specialization' },
                { name: 'Ibrahim Shaikh', src: 'images/people/Placeholder.jpg', role: 'Control and Power Team Member - Electrical', year: '5th Year Electrical Engineering' },
                { name: 'Ying Wan', src: 'images/people/Ying.jpeg', role: 'Control and Power Team Member - Software', year: '2nd Year Computer Engineering, Software Specialization' },
                { name: 'Gary Ng Kwong Sang', src: 'images/people/Gary.jpg', role: 'Control and Power Team Member - Software', year: '4th Year Computer Science' }
                // { name: 'Laura Petrich', src: 'images/people/Laura.jpg', role: 'Control and Power Team Manager', year: '4th Year Computer Science, Honors' },
                //{ name: 'Taylor Zowtuk', src: 'images/people/Taylor.jpg', role: 'Control and Power Lead - Software', year: '3rd Year Computing Science, After Degree' },
                //{ name: 'Cyrus Diego', src: 'images/people/Cyrus.jpg', role: 'Control and Power Lead - Hardware', year: '3rd Year Computer Engineering, Software Specialization' },
                //{ name: 'Adil Younus', src: 'images/people/Adil.jpg', role: 'Control and Power Lead - Power', year: '2nd Year Electrical Engineering' },
                //{ name: 'Qiulin Yu', src: 'images/people/Qiulin.jpg', role: 'Control and Power Team Member', year: '3rd Year Mechanical Engineering' },
                //{ name: 'Jacob Reckhard', src: 'images/people/Jacob.jpg', role: 'Control and Power Team Member', year: '4th Year Mechanical Engineering' },
            
            ]
        },
        {
            title: 'Biomechanical Team',
            blurb: 'The Biomechanical team is working on the structural design of the exoskeleton. They investigate human motion and work to build an ergonomic and effective suit that the Control and Power team can bring to life.',
            members: [
                
                //{ name: 'Isobel Tetreau', src: 'images/people/Isobel.jpg', role: 'Biomechanics Team Manager', year: '4th Year Mechanical Engineering, Biomedical Specialization' },
                { name: 'Brianna Tolsma', src: 'images/people/Placeholder.jpg', role: 'Biomechanical Team Lead', year: '3rd Year Mechanical Engineering, Biomedical Specialization' },
                /*
                { name: 'Eric Kwas', src: 'images/people/Eric.jpg', role: 'Biomechanics Team Member, Lower Arm and Elbow', year: '2nd Year Mechanical Engineering' },
                { name: 'Femi Akinola', src: 'images/people/Femi.jpg', role: 'Biomechanics Team Member, Lower Arm', year: '3rd Year Mechanical Engineering' },
                { name: 'Mehtab Malik', src: 'images/people/Placeholder.jpg', role: 'Biomechanics Team Member, Elbow', year: '4th Year Mechanical Engineering' },
                { name: 'Warren Leung Kam Tsang', src: 'images/people/Warren.jpg', role: 'Biomechanics Team Member', year: '4th Year Mechanical Engineering' },
                //{ name: 'Ahmed Abd El-Gelil', src: 'images/people/Ahmed.png', role: 'Biomechanics Team Lead', year: '3rd Year Mechanical Engineering, Biomedical Specialization' },
                { name: 'Xiao Meng', src: 'images/people/Xiao.jpg', role: 'Biomechanics Team Lead', year: '3rd Year Mechanical Engineering, Biomedical Specialization' },
                { name: 'Tully Underhill', src: 'images/people/Tully.jpg', role: 'Biomechanics Team Lead', year: '3rd Year Mechanical Engineering, Biomedical Specialization' },
                { name: 'Isaiah Wong', src: 'images/people/Isaiah.jpg', role: 'Biomechanics Team Member - Motor Mount Specialist', year: '3rd Year Mechanical Engineering' },
                { name: 'Kiernan Carroll', src: 'images/people/Kiernan.jpg', role: 'Biomechanics Team Member - Motor Mount Specialist', year: '3rd Year Mechanical Engineering' },
                */
               { name: 'Anakin Gill', src: 'images/people/anakin.png', role: 'Biomechanical Team Member', year: '2nd Year Mechanical Engineering, Biomedical Specialization', },
               { name: 'Irina Manuel', src: 'images/people/Placeholder', role: 'Biomechanical Team Member', year: '2nd Year Mechanical Engineering', },
               { name: 'Eric Kwas', src: 'images/people/Eric.jpg', role: 'Biomechanical Team Member', year: '3rd Year Mechanical Engineering, Biomedical Specialization', },
               { name: 'Robyn de Wet', src: 'images/people/robyn_de_wet.png', role: 'Biomechanical Team Member', year: '3rd Year Mechanical Engineering', },
               { name: 'Madeleine Barton-Keener', src: 'images/people/madeleine.jpg', role: 'Biomechanical Team Member', year: '2nd Year Mechanical Engineering', },
               { name: 'Colleen Lam', src: 'images/people/colleen.png', role: 'Biomechanical Team Member', year: '2nd Year Mechanical Engineering', },
               { name: 'Golie Masoumian', src: 'images/people/golie.png', role: 'Biomechanical Team Member', year: '3rd Year Mechanical Engineering', }
            ]
        },
        {
            title: 'Commercial Team',
            blurb: 'The Commercial team works on securing corporate sponsorships, assessing the marketability of the device, and budgeting for the teams prototyping.',
            members: [
                // { name: 'Josh Lau', src: 'images/people/Josh.jpg', role: 'Commercial Team Lead', year: '4th year Mechanical Engineering' },
                // { name: 'Victor Egruen-Echaiz', src: 'images/people/Victor.jpg', role: 'Commercial Team Lead', year: '3rd Year Business, Human Resources Major' },
                // { name: 'Sunny Yang', src: 'images/people/Sunny.jpg', role: 'Commercial Team Member', year: '2nd Year Civil Engineering' },
                {name: 'Andy Lee', src: 'images/people/andylee.jpg', role: 'Commercial Team Lead', year: '4th Year Specialization in Psychology, Minor in Business'},
                {name: 'Minh Luu', src: 'images/people/Placeholder.jpg', role: 'Commercial Team Member', year: '2nd Year Mechanical Engineering, Biomedical Specialization'}
            ]
        },
        {
            title: '3D Wrist Project Team',
            blurb: 'The 3D Wrist Project Team is designing and developing a 3D-printed synthetic wrist model, composed of synthetic bone and ligaments with similar anatomical and biomechanical properties as those of a human wrist.',
            members: [
                { name: 'Taylor Bulbuc', src: 'images/people/TaylorB.jpg', role: '3D Wrist Project Team Lead', year: '5th Year Mechanical Engineering, Biomedical Specialization'},
                { name: 'Isaiah Wong', src: 'images/people/Isaiah2.jpg', role: '3D Wrist Project Team Member', year: '4th Year Mechanical Engineering, Biomedical Specialization'},
                { name: 'Tully Underhill', src: 'images/people/Placeholder.jpg', role: '3D Wrist Project Team Member', year: '4th Year Mechanical Engineering, Biomedical Specialization'},
                { name: 'Rushi Patel', src: 'images/people/Rushi_Patel.jpg', role: '3D Wrist Project Team Member', year: '3rd Year Mechanical Engineering'},
                { name: 'Hersh Srivastava', src: 'images/people/Hersh.jpg', role: '3D Wrist Project Team Member', year: '3rd Year Civil Engineering'},
                { name: 'Yahia Elsayed', src: 'images/people/Yahia.jpg', role: '3D Wrist Project Team Member', year: '3rd Year Mechanical Engineering'}
            ]
        },
        {
            title: 'Executive Team',
            blurb: 'The executive team is working on making sure everything is going along smoothly, and nothing gets missed.',
            members: [
                { name: 'Adil Younus', src: 'images/people/Adil.jpg', role: 'President', year: '3rd Year Electrical Engineering' },
                { name: 'Weilin Qiu', src: 'images/people/Weilin.jpg', role: 'VP Communications, Mechanical Team Member', year: '3rd Year Mechanical Engineering' },
                { name: 'Ben Hallworth', src: 'images/people/Ben.jpg', role: 'Ex-President, Founder', year: '4th Year Mechanical Engineering, Biomedical Specialization' },
                { name: 'Alicia MacDonald', src: 'images/people/Alicia.jpg', role: 'Ex-President, Founder', year: '4th Year Mechanical Engineering, Biomedical Specialization' },
                //{ name: 'Aabid Wadood', src: 'images/people/Aabid.jpg', role: 'VP External', year: '3rd Year Mechanical Engineering, Biomedical Specialization' },
                //{ name: 'Qibang Feng', src: 'images/people/Qibang.jpg', role: 'VP Finance', year: '4th Year Finance Major, Economics Minor' },
            ]
        },
    ]
</script>
