// ==========================================
// DISASTER RELIEF SYSTEM - script.js
// ==========================================


// ==========================================
// 1. DISASTER REQUEST
// ==========================================

const requestForm = document.getElementById("requestForm");

if (requestForm) {

    requestForm.addEventListener("submit", async function (event) {

        event.preventDefault();

        const requester = document.getElementById("requester").value.trim();
        const location = document.getElementById("location").value.trim();
        const type = document.getElementById("type").value;
        const severity = Number(document.getElementById("severity").value);
        const people = Number(document.getElementById("people").value);

        const message = document.getElementById("message");

        const { data, error } = await supabaseClient
            .from("requests")
            .insert([
                {
                    requester: requester,
                    location: location,
                    type: type,
                    severity: severity,
                    people: people
                }
            ]);

        if (error) {

            console.error("Request Error:", error);

            message.textContent = "Error submitting request.";

        } else {

            message.textContent = "Request submitted successfully!";

            requestForm.reset();
        }
    });
}


// ==========================================
// 2. LOAD REQUESTS
// ==========================================

async function loadRequests() {

    const { data, error } = await supabaseClient
        .from("requests")
        .select("*")
        .order("created_at", { ascending: false });

    if (error) {

        console.error("Error loading requests:", error);
        return;
    }

    console.log("Requests:", data);

    const requestList = document.getElementById("requestList");

    if (!requestList) {
        return;
    }

    requestList.innerHTML = "";

    data.forEach(function (request) {

        const row = document.createElement("div");

        row.innerHTML = `
            <p>
                <strong>${request.requester}</strong>
                - ${request.location}
                - ${request.type}
                - Severity: ${request.severity}
                - People: ${request.people}
                - Status: ${request.status}
            </p>
        `;

        requestList.appendChild(row);
    });
}


// ==========================================
// 3. ADD RESOURCE
// ==========================================

const resourceForm = document.getElementById("resourceForm");

if (resourceForm) {

    resourceForm.addEventListener("submit", async function (event) {

        event.preventDefault();

        const name = document.getElementById("resourceName").value.trim();
        const category = document.getElementById("resourceCategory").value;
        const quantity = Number(
            document.getElementById("resourceQuantity").value
        );

        const message = document.getElementById("resourceMessage");

        const { data, error } = await supabaseClient
            .from("resources")
            .insert([
                {
                    name: name,
                    category: category,
                    quantity: quantity
                }
            ]);

        if (error) {

            console.error("Resource Error:", error);

            if (message) {
                message.textContent = "Error adding resource.";
            }

        } else {

            if (message) {
                message.textContent = "Resource added successfully!";
            }

            resourceForm.reset();

            loadResources();
        }
    });
}


// ==========================================
// 4. LOAD RESOURCES
// ==========================================

async function loadResources() {

    const { data, error } = await supabaseClient
        .from("resources")
        .select("*")
        .order("created_at", { ascending: false });

    if (error) {

        console.error("Error loading resources:", error);
        return;
    }

    console.log("Resources:", data);

    const resourceList = document.getElementById("resourceList");

    if (!resourceList) {
        return;
    }

    resourceList.innerHTML = "";

    data.forEach(function (resource) {

        const row = document.createElement("div");

        row.innerHTML = `
            <p>
                <strong>${resource.name}</strong>
                - Category: ${resource.category}
                - Quantity: ${resource.quantity}
            </p>
        `;

        resourceList.appendChild(row);
    });
}


// ==========================================
// 5. ADD RELIEF TEAM
// ==========================================

const teamForm = document.getElementById("teamForm");

if (teamForm) {

    teamForm.addEventListener("submit", async function (event) {

        event.preventDefault();

        const name = document.getElementById("teamName").value.trim();
        const leader = document.getElementById("teamLeader").value.trim();
        const location = document.getElementById("teamLocation").value.trim();

        const message = document.getElementById("teamMessage");

        const { data, error } = await supabaseClient
            .from("teams")
            .insert([
                {
                    name: name,
                    leader: leader,
                    location: location,
                    status: "Available"
                }
            ]);

        if (error) {

            console.error("Team Error:", error);

            if (message) {
                message.textContent = "Error adding team.";
            }

        } else {

            if (message) {
                message.textContent = "Team added successfully!";
            }

            teamForm.reset();

            loadTeams();
        }
    });
}


// ==========================================
// 6. LOAD TEAMS
// ==========================================

async function loadTeams() {

    const { data, error } = await supabaseClient
        .from("teams")
        .select("*")
        .order("created_at", { ascending: false });

    if (error) {

        console.error("Error loading teams:", error);
        return;
    }

    console.log("Teams:", data);

    const teamList = document.getElementById("teamList");

    if (!teamList) {
        return;
    }

    teamList.innerHTML = "";

    data.forEach(function (team) {

        const row = document.createElement("div");

        row.innerHTML = `
            <p>
                <strong>${team.name}</strong>
                - Leader: ${team.leader}
                - Location: ${team.location}
                - Status: ${team.status}
            </p>
        `;

        teamList.appendChild(row);
    });
}


// ==========================================
// 7. DASHBOARD COUNTS
// ==========================================

async function loadDashboard() {

    const { count: requestCount, error: requestError } =
        await supabaseClient
            .from("requests")
            .select("*", { count: "exact", head: true });

    const { count: resourceCount, error: resourceError } =
        await supabaseClient
            .from("resources")
            .select("*", { count: "exact", head: true });

    const { count: teamCount, error: teamError } =
        await supabaseClient
            .from("teams")
            .select("*", { count: "exact", head: true });


    if (requestError) {
        console.error(requestError);
    }

    if (resourceError) {
        console.error(resourceError);
    }

    if (teamError) {
        console.error(teamError);
    }


    const requestCountElement =
        document.getElementById("requestCount");

    const resourceCountElement =
        document.getElementById("resourceCount");

    const teamCountElement =
        document.getElementById("teamCount");


    if (requestCountElement) {
        requestCountElement.textContent = requestCount || 0;
    }

    if (resourceCountElement) {
        resourceCountElement.textContent = resourceCount || 0;
    }

    if (teamCountElement) {
        teamCountElement.textContent = teamCount || 0;
    }
}


// ==========================================
// 8. RUN FUNCTIONS WHEN PAGE LOADS
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    loadRequests();

    loadResources();

    loadTeams();

    loadDashboard();

});