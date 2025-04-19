async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("http://127.0.0.1:8000/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });

        if (!response.ok) {
            throw new Error("Invalid login credentials");
        }

        const data = await response.json();
        localStorage.setItem("auth_token", data.token);  // ✅ Store token
        alert("Login Successful!");
        window.location.href = "dashboard.html";  // ✅ Redirect to dashboard
    } catch (error) {
        alert(error.message);
    }
}
