<template>
    <NavBar :token="this.token"/>
    <div id="tos">
        <h1>Terms Of Service</h1>
        <hr>
        <p>
            Please read these terms of service ("terms of service", "terms") carefully before using our
            website (“website”, "service") operated by Mentorprise ("us", 'we", "our").
        </p>
        <h2>Conditions of Use</h2>
        <p>
            By using this website, you certify that you have read and reviewed this Agreement and that you
            agree to comply with its terms. If you do not want to be bound by the terms of this Agreement,
            you are advised to leave the website accordingly. Mentorprise only grants use and access of this
            website, its products, and its services to those who have accepted its terms.
        </p>

        <h2>Privacy Policy</h2>
        <p>
            Before you continue using our website, we advise you to read our <router-link :to="'/Privacy?t='+this.token">privacy policy</router-link> regarding our user data collection. It will help you better understand our practices.
        </p>

        <h2>Age Restriction</h2>
        <p>
            You must be at least 18 (eighteen) years of age before you can use this website. By using this
            website, you warrant that you are at least 18 years of age and you may legally adhere to this
            Agreement. Mentorprise assumes no responsibility for liabilities related to age misrepresentation.
        </p>

        <h2>Intellectual Property</h2>
        <p>
            You agree that all materials, products, and services provided on this website are the property of
            Mentorprise, its affiliates, directors, officers, employees, agents, suppliers, or licensors including all
            copyrights, trade secrets, trademarks, patents, and other intellectual property. You also agree
            that you will not reproduce or redistribute the Mentorprise’s intellectual property in any way,
            including electronic, digital, or new trademark registrations.
            <br><br>
            You grant Mentorprise a royalty-free and non-exclusive license to display, use, copy, transmit, and
            broadcast the content you upload and publish. For issues regarding intellectual property claims,
            you should contact the company in order to come to an agreement.
        </p>

        <h2>User Accounts</h2>
        <p>
            As a user of this website, you may be asked to register with us and provide private information.
            You are responsible for ensuring the accuracy of this information, and you are responsible for
            maintaining the safety and security of your identifying information. You are also responsible for
            all activities that occur under your account or password.
            <br><br>
            If you think there are any possible issues regarding the security of your account on the website,
            inform us immediately so we may address it accordingly.
            <br><br>
            We reserve all rights to terminate accounts, edit or remove content and cancel orders in their
            sole discretion.
        </p>


        <h2>Applicable Law</h2>
        <p>
            By visiting this website, you agree that the laws of the United Kingdom, without regard to principles of
            conflict laws, will govern these terms and conditions, or any dispute of any sort that might come
            between Mentorprise and you, or its business partners and associates. 
        </p>

        <h2>Disputes</h2>
        <p>
            Any dispute related in any way to your visit to this website or to products you purchase from us
            shall be arbitrated by state or federal court United Kingdom and you consent to exclusive jurisdiction
            and venue of such courts.
        </p>

        <h2>Indemnification</h2>
        <p>
            You agree to indemnify Mentorprise and its affiliates and hold Mentorprise harmless against legal claims
            and demands that may arise from your use or misuse of our services. We reserve the right to
            select our own legal counsel.
        </p>

        <h2>Limitation on liability</h2>
        <p>
            Mentorprise is not liable for any damages that may occur to you as a result of your misuse of our
            website.
            <br><br>
            Mentorprise reserves the right to edit, modify, and change this Agreement any time. We shall let our
            users know of these changes through electronic mail. This Agreement is an understanding
            between Mentorprise and the user, and this supersedes and replaces all prior agreements regarding
            the use of this website.
        </p>
    </div>
</template>

<script>
    import NavBar from "../components/Navbar.vue"
    export default {
        name: "TOS",
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
    #tos {
        color: white;
        padding: 5%;
    }
    hr {
        border: solid 2px white;
    }
</style>