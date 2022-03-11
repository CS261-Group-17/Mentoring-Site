<template>
    <NavBar :token="this.token"/>
    <div id="privacy">
        <h1>Privacy</h1>
        <hr>
        <p>
            This privacy policy will explain how Mentorprise uses the personal data we collect from you when you use our website.
        </p>
        <h2>What data do we collect?</h2>
        <p>Our company collects the following data:</p>
        <ul>
            <li>Personal identification information, including but not limited to: full names; email addresses; job titles</li>
            <li>Data relevant to the running of the site, including but not limited to: self-assessed strengths and weaknesses, user biographies, scheduled meeting times</li>
        </ul>

        <h2>How do we collect your data?</h2>
        <p>You directly provide Our Company with most of the data we collect. We collect data and process data when you:</p>
        <ul>
            <li>Register online or place an order for any of our products or services.</li>
            <li>Voluntarily complete a customer survey or provide feedback on any of our message boards or via email.</li>
            <li>Use or view our website via your browser’s cookies.</li>
        </ul>

        <h2>How will we use your data?</h2>
        <p>Our Company collects your data so that we can provide mentorship capabilities and manage your account.</p>
    
        <h2>How do we store your data?</h2>
        <p>
            Our Company securely stores your data at our servers in the United Kingdom, protected using password authentication.
            <br><br>
            Our Company will keep your user data whilst your account is open. Once your account is deleted, we will delete all data about or referencing your account.
        </p>

        <h2>What are your data protection rights?</h2>
        <p>Our Company would like to make sure you are fully aware of all of your data protection rights. Every user is entitled to the following:</p>
        <ul>
            <li><b>The right to access</b> – You have the right to request Our Company for copies of your personal data. We may charge you a small fee for this service.</li>
            <li><b>The right to rectification</b> – You have the right to request that Our Company correct any  information you believe is inaccurate. You also have the right to  request Our Company to complete the information you believe is incomplete.</li>
            <li><b>The right to erasure</b> – You have the right to request that Our Company erase your personal data, under certain conditions.</li>
            <li><b>The right to restrict processing</b> – You have the right to request that Our Company restrict the processing of your personal data, under certain conditions.</li>
            <li><b>The right to object to processing</b> – You have the right to object to Our Company’s processing of your personal data, under certain conditions.</li>
            <li><b>The right to data portability</b> – You have the right to request that Our Company transfer the data that we have collected to another organization, or directly to you, under  certain conditions.</li>
        </ul>

        <p>If you make a request, we have one month to  respond to you. If you would like to exercise any of these rights,  please contact us at our email: u2006527@live.warwick.ac.uk</p>
    
        <h2>Cookies</h2>
        <p>
            Cookies are text files placed on your computer to collect standard Internet log information and visitor behaviour information. When you visit our  websites, we may collect information from you automatically through  cookies or similar technology
            <br><br>
            For further information, visit <a href="https://www.allaboutcookies.org/">allaboutcookies.org</a>.
        </p>

        <h2>How do we use cookies?</h2>
        <p>Our Company uses cookies in a range of ways to improve your experience on our website, including:</p>
        <ul>
            <li>Keeping you signed in</li>
            <li>Understanding how you use our website</li>
        </ul>

        <h2>What types of cookies do we use?</h2>
        <p>There are a number of different types of cookies, however, our website uses:</p>
        <ul>
            <li>Functionality – Our Company uses these cookies so that we recognize you on our  website and remember your previously selected preferences. These could  include what language you prefer and location you are in. A mix of  first-party and third-party cookies are used.</li>
        </ul>
        <p>Our website does not use advertising cookies.</p>
        
        <h2>How to manage cookies</h2>
        <p>You can set your browser not to accept cookies, and the above website tells you how to remove cookies from your browser. However, in a few cases,  some of our website features may not function as a result.</p>

        <h2>Privacy policies of other websites</h2>
        <p>The Mentorprise website contains links to other websites. Our privacy  policy applies only to our website, so if you click on a link to another website, you should read their privacy policy.</p>

        <h2>Changes to our privacy policy</h2>
        <p>Our Company keeps its privacy policy under regular review and places any  updates on this web page. This privacy policy was last updated on 2022/03/08.</p>

        <h2>How to contact us</h2>
        <p>
            If you have any questions  about Our Company’s privacy policy, the data we hold on you, or you  would like to exercise one of your data protection rights, please do not hesitate to contact us.
            <br><br>
            Email us at: u2006527@live.warwick.ac.uk
        </p>

        <h2>How to contact the appropriate authority</h2>
        <p>Should you wish to report a complaint or if you feel that Our Company has not  addressed your concern in a satisfactory manner, you may contact the Information Commissioner’s Office.</p>
    </div>
</template>

<script>
    import NavBar from "../components/Navbar.vue"
    export default {
        name: "privacy",
        components: {
            NavBar
        },
        data() {
            return {
                token: {}
            }
        },
        created() {
            let splitURL = document.URL.split("?")
            let failed = true
            if(splitURL.length > 1) {
            let urlParams = new URLSearchParams("?" + splitURL[1])
            if(urlParams.has("t")) {
                this.token = urlParams.get("t")
                //alert(this.token)
                failed = false
            }
            }
            if(failed) {
                this.$router.push("/")
            }
        }
    }
</script>

<style scoped>
    h1 {
        font-weight: 800;
    }
    #privacy {
        color: white;
        padding: 5%;
    }
    hr {
        border: solid 2px white;
    }
</style>