// ✅ Check Authentication Before Fetching Data
async function fetchFaultData() {
    const token = localStorage.getItem("auth_token");  // Get token from storage
    if (!token) {
        alert("You are not logged in. Redirecting to login...");
        window.location.href = "login.html";  // Redirect to login page
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/fault-detection", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify({ machine_id: "MACHINE_001" })
        });

        if (!response.ok) {
            throw new Error("Error fetching data. Please check authentication.");
        }

        const data = await response.json();
        displayData(data);
    } catch (error) {
        alert(error.message);
        console.error("Error:", error);
    }
}

// ✅ Display Data on Dashboard
function displayData(data) {
    document.getElementById("machine_id").innerText = `Machine ID: ${data.machine_id}`;
    document.getElementById("fault_detected").innerText = `Fault Detected: ${data.fault_detected}`;
    document.getElementById("temperature").innerText = `Temperature: ${data.temperature}°C`;
    document.getElementById("vibration").innerText = `Vibration: ${data.vibration} m/s²`;
    document.getElementById("pressure").innerText = `Pressure: ${data.pressure} Pa`;
    document.getElementById("confidence").innerText = `Confidence: ${data.confidence}%`;
    document.getElementById("suggested_action").innerText = `Suggested Action: ${data.suggested_action}`;
}

// ✅ Call Fetch Function on Page Load
window.onload = fetchFaultData;
{
const token = localStorage.getItem("auth_token");

    if (!token) {
        alert("You are not logged in! Redirecting to login page...");
        window.location.href = "login.html";  // Force redirect to login
        return;
    }

    fetchFaultData();  // If authenticated, load data
};
