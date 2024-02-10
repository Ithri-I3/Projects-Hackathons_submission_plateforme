const form = document.querySelector("#logInForm")
form.addEventListener("submit", async (e) => {
    const usernameInput = document.getElementById("yourUsername").value;
    const passwordInput = document.getElementById("yourPassword").value;

    const res = await fetch("http://localhost:8080", {
        method: "POST",
        headers: {
            'Content-Type' : "application/json"
        },
        body: JSON.stringify({
            username : usernameInput
            , password : passwordInput
        }),
    })
    const data = await res.json()

})