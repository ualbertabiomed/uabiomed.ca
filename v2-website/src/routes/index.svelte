<section id="banner">
    <div class="content">
        <header>
            <h1>University of Alberta Biomedical Technologies Development Group</h1>
            <p>An undergraduate student group for those interested in medicine, engineering, and science.</p>
        </header>
        <p>
            UAlberta Biomed is a student group for innovative and hardworking
            students who are interested in creating solutions in the medicine,
            engineering, and science fields of study. Whether you're an
            engineering student, a science student, or a business student,
            UAlberta Biomed is the club for you. Our group encourages new and
            creative ideas to be explored.
        </p>
        <ul class="actions">
            <li><a href="#learn-more" class="button big">Learn More</a></li>
        </ul>
    </div>
    <span class="image object video">
         <video src="video.mp4" width="480" controls> </video>
    </span>
</section>
<section id="learn-more">
    <header class="major">
        <h2>Our Plan</h2>
    </header>
    <div class="features">
        <article>
            <span class="icon fa-diamond"></span>
            <div class="content">
                <h3><a href="https://venturewell.org/debut/">The Competition</a></h3>
                <p>
                    DEBUT is a US based competition, strictly for undergraduate
                    students. The competition requires teams to identify a
                    clinical problem and build a fully functional prototype to
                    solve it. The deadline for submission is May 2020.<br>For
                    more information, visit https://venturewell.org/debut/
                </p>
            </div>
        </article>
        <article>
            <span class="icon fa-paper-plane"></span>
            <div class="content">
                <h3><a href="/exoskeleton">The Project</a></h3>
                <p>
                    The team's current project is designing and prototyping an
                    exoskeleton for the workplace. The purpose of the
                    exoskeleton is to correct posture and reduce the load for
                    the back and shoulders. The exoskeleton will be able to
                    give users a 33% mechanical advantage, up to a full lift of
                    75lbs. This exoskeleton will also track motion and give
                    feedback to the user to prevent repetitive motion injuries
                    and unhealthy range of motion injuries.
                </p>
            </div>
        </article>
        <article>
            <span class="icon fa-users"></span>
            <div class="content">
                <h3><a href="/team">The Team</a></h3>
                <p>
                    Joining our group will not only provide you with invaluable
                    research experience. You will also gain great team building
                    experience. On top of this, you will have the opportunity
                    to meet unique and inspiring individuals.
                </p>
            </div>
        </article>
        <article>
            <span class="icon fa-code-fork"></span>
            <div class="content">
                <h3>The Future</h3>
                <p>
                    With ALEX being our first major project, we hope to
                    develop various biomedical technologies in the upcoming
                    years. Optimizing ALEX dc to pneumatic optimizing
                    devices for prosthetic users.
                </p>
            </div>
        </article>
    </div>
</section>
<section>
    <h2> Sponsors </h2>
    <div class='row'>
        {#each sponsors as member}
            <Sponsor {...member}/>
        {/each}
    </div>
</section>

<style>
.video {
    display: flex!important;
    justify-content: center;
    align-items: center;
}
</style>

<script>
    import Sponsor from '../components/sponsor.svelte'
    let sponsors = [
        { name: 'Faculty of Engineering', src: 'images/engg_logo.png', role: 'Gold Tier Sponsor' },
        { name: 'Students Union', src: 'images/uofa_su.png', role: 'Gold Tier Sponsor' },
    ]
</script>
