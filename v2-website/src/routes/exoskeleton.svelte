<style>
    .hor {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .page {
        width: 80%;
        margin-left: 10%;
        margin-top: 50px;
    }
    img {
        margin: 0 20px;
        padding: 10px;
    }
    .img1 {
        max-width: 20vw;
    }
    .img2 {
        margin: 0;
        max-width: 35vw;
    }
</style>
<div class="page">
    <h2> ALEX - The Exoskeleton </h2>
    <div class="hor">
        <p>
            ALEX (ALberta EXoskeleton) will be a powered, upper body exoskeleton.
            Preliminary prototypes will be 3D printed and powered with DC motors and
            later prototypes will be machined from aluminum and powered with DC motors
            and / or pneumatic muscles.  ALEX’s arm has been designed, printed and
            tested over the summer. Some features include a pawl and ratchet mechanism
            as a fail safe if the suit were to lose power and a sliding wrist component
            to reduce friction between the user and the suit.
        <p>

        <div>
            <img src="/images/elbow-real.png" class="img1">
        </div>
    </div>

    <div class="hor">
        <div>
            <img src="/images/elbow-fake.png" class="img2">
        </div>
        <p>
            On the controls side, the original source code for the project is
            currently stored in the UAlberta Biomed Github repository. The
            source files stored in the repository is used to program the ODrive
            and Arduino microcontrollers to control the motors for the
            exoskeleton.  We have code that allows Arduino to communicate with
            the motors using the ODrive, and in the future, we will be adding
            PID control and gravity compensation.
        </p>

    </div>
    <p>
        The design will extend to the shoulder and back / hips in the 2019/2020
        school year creating vast opportunities for a wide variety of students to
        get involved in solid modelling, simulations, coding the control systems,
        3D printing, and testing of the structure and control systems.
    </p>
</div>
