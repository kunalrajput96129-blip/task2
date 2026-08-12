/* ==========================================================================
   GOVDIRECT DIGITAL SERVICES PORTAL - INTERACTIVITY ENGINE
   Client-Side Logic, Universal Accessibility, Multi-step Form & Tracker
   ========================================================================== */

// 1. MOCK SERVICE CATALOG DATA
const SERVICES_DATA = [
    {
        id: "srv-1",
        title: "Driver License Renewal",
        category: "Identity",
        sla: "10 Mins",
        desc: "Instant digital renewal for personal & commercial driver licenses with automated national database photo check.",
        fee: "$35.00",
        features: "✓ Instant Pass Generation • WCAG AAA",
        popular: true
    },
    {
        id: "srv-2",
        title: "Business Name Registration",
        category: "Business",
        sla: "1 Day",
        desc: "Register commercial trade names, receive state tax ID clearance, and download official certificate of incorporation.",
        fee: "$120.00",
        features: "✓ EIN Integration • Automated Name Check",
        popular: true
    },
    {
        id: "srv-3",
        title: "Citizen Healthcare Grant",
        category: "Healthcare",
        sla: "3 Days",
        desc: "Apply for state-subsidized medical coverage, prescription discounts, and family health welfare grants.",
        fee: "Free",
        features: "✓ Low-Income Subsidy • Family Plan",
        popular: true
    },
    {
        id: "srv-4",
        title: "Property Tax Valuation",
        category: "Housing",
        sla: "Instant",
        desc: "Calculate municipal property tax assessments, file exemption claims, and generate official payment receipts.",
        fee: "Free",
        features: "✓ Instant Appraisal • Exemption Filing",
        popular: true
    },
    {
        id: "srv-5",
        title: "Building Construction Permit",
        category: "Business",
        sla: "5 Days",
        desc: "Submit structural blueprints and environmental impact assessments for municipal engineering clearance.",
        fee: "$250.00",
        features: "✓ Blueprint Inspection • Engineering Review",
        popular: false
    },
    {
        id: "srv-6",
        title: "Passport Express Renewal",
        category: "Identity",
        sla: "2 Days",
        desc: "Schedule biometric verification appointments and expedite international biometric travel document issuance.",
        fee: "$85.00",
        features: "✓ Biometric Booking • Expedited Processing",
        popular: false
    }
];

// STATE MANAGEMENT
let currentFontScale = 1.0;
let currentFilter = "all";
let currentStep = 1;
let selectedService = null;
let ttsActive = false;

// DOM ELEMENT REFERENCES
document.addEventListener("DOMContentLoaded", () => {
    initServiceCatalog();
    initAccessibilityControls();
    initFilterTabs();
    initSearchWidget();
    initModalWorkflows();
    initTrackerSystem();
});

// 2. RENDER SERVICE CATALOG CARDS
function initServiceCatalog() {
    const container = document.getElementById("services-container");
    if (!container) return;

    renderCards(SERVICES_DATA);
}

function renderCards(servicesList) {
    const container = document.getElementById("services-container");
    container.innerHTML = "";

    if (servicesList.length === 0) {
        container.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 40px; background: var(--color-card-bg); border-radius: 12px;">
                <h3>No matching digital services found</h3>
                <p style="color: var(--color-text-muted);">Try adjusting your search keywords or selecting 'All Services'.</p>
            </div>
        `;
        return;
    }

    servicesList.forEach(srv => {
        const card = document.createElement("article");
        card.className = "service-card";
        card.innerHTML = `
            <div class="card-top">
                <div class="card-meta">
                    <span class="cat-badge">${srv.category}</span>
                    <span class="sla-tag">⏱️ SLA: ${srv.sla}</span>
                </div>
                <h3 class="card-title">${srv.title}</h3>
                <p class="card-desc">${srv.desc}</p>
                <div class="card-features">${srv.features}</div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 16px;">
                <span style="font-weight: 700; font-size: 0.9rem;">Fee: ${srv.fee}</span>
                <button class="btn btn-primary btn-apply" data-id="${srv.id}" aria-label="Apply for ${srv.title}">
                    Apply Now ➔
                </button>
            </div>
        `;
        container.appendChild(card);
    });

    // Attach click listeners to "Apply Now" buttons
    document.querySelectorAll(".btn-apply").forEach(btn => {
        btn.addEventListener("click", (e) => {
            const srvId = e.currentTarget.getAttribute("data-id");
            openApplicationModal(srvId);
        });
    });
}

// 3. UNIVERSAL ACCESSIBILITY CONTROLS
function initAccessibilityControls() {
    const btnAdd = document.getElementById("btn-font-add");
    const btnSub = document.getElementById("btn-font-sub");
    const btnReset = document.getElementById("btn-font-reset");
    const btnContrast = document.getElementById("btn-contrast-toggle");
    const btnMotion = document.getElementById("btn-motion-toggle");
    const btnTTS = document.getElementById("btn-tts-toggle");

    // Font Scaling Logic
    btnAdd.addEventListener("click", () => updateFontScale(0.1));
    btnSub.addEventListener("click", () => updateFontScale(-0.1));
    btnReset.addEventListener("click", () => {
        currentFontScale = 1.0;
        document.documentElement.style.setProperty("--font-scale", "1.0");
        showToast("Font size reset to default (100%)");
    });

    // Dark High Contrast Toggle
    btnContrast.addEventListener("click", () => {
        const currentTheme = document.documentElement.getAttribute("data-theme");
        const newTheme = currentTheme === "dark" ? "light" : "dark";
        document.documentElement.setAttribute("data-theme", newTheme);
        document.getElementById("contrast-icon").textContent = newTheme === "dark" ? "☀️" : "🌙";
        showToast(`Theme switched to ${newTheme.toUpperCase()} mode`);
        announceToScreenReader(`High contrast theme switched to ${newTheme} mode`);
    });

    // Reduced Motion Toggle
    btnMotion.addEventListener("click", () => {
        const currentMotion = document.documentElement.getAttribute("data-motion");
        const newMotion = currentMotion === "reduced" ? "normal" : "reduced";
        document.documentElement.setAttribute("data-motion", newMotion);
        showToast(`Motion reduction set to: ${newMotion.toUpperCase()}`);
    });

    // Text to Speech Voice Simulation
    btnTTS.addEventListener("click", () => {
        ttsActive = !ttsActive;
        btnTTS.style.backgroundColor = ttsActive ? "#d97706" : "#059669";
        btnTTS.textContent = ttsActive ? "🔊 Screen Reader Active" : "🔊 Text-to-Speech Preview";
        showToast(ttsActive ? "Screen Reader Voice Simulation ON" : "Screen Reader Simulation OFF");

        if (ttsActive && 'speechSynthesis' in window) {
            const utter = new SpeechSynthesisUtterance("GovDirect Public Services Portal. Accessibility Assistant active. Use tab key to navigate.");
            window.speechSynthesis.speak(utter);
        }
    });
}

function updateFontScale(delta) {
    currentFontScale = Math.min(Math.max(currentFontScale + delta, 0.8), 1.4);
    document.documentElement.style.setProperty("--font-scale", currentFontScale.toFixed(2));
    showToast(`Font scaling: ${Math.round(currentFontScale * 100)}%`);
}

// 4. CATEGORY FILTERS & SEARCH
function initFilterTabs() {
    const tabs = document.querySelectorAll(".filter-tab");
    tabs.forEach(tab => {
        tab.addEventListener("click", (e) => {
            tabs.forEach(t => {
                t.classList.remove("active");
                t.setAttribute("aria-selected", "false");
            });
            e.currentTarget.classList.add("active");
            e.currentTarget.setAttribute("aria-selected", "true");

            currentFilter = e.currentTarget.getAttribute("data-category");
            applyFilters();
        });
    });
}

function initSearchWidget() {
    const input = document.getElementById("service-search-input");
    const btnSearch = document.getElementById("btn-search-trigger");
    const chips = document.querySelectorAll(".chip");

    input.addEventListener("input", applyFilters);
    btnSearch.addEventListener("click", applyFilters);

    chips.forEach(chip => {
        chip.addEventListener("click", (e) => {
            const term = e.currentTarget.getAttribute("data-filter");
            input.value = term;
            applyFilters();
        });
    });
}

function applyFilters() {
    const searchTerm = document.getElementById("service-search-input").value.toLowerCase();
    
    const filtered = SERVICES_DATA.filter(srv => {
        const matchesCategory = currentFilter === "all" || srv.category === currentFilter;
        const matchesSearch = srv.title.toLowerCase().includes(searchTerm) || 
                              srv.desc.toLowerCase().includes(searchTerm) || 
                              srv.category.toLowerCase().includes(searchTerm);
        return matchesCategory && matchesSearch;
    });

    renderCards(filtered);
}

// 5. MULTI-STEP MODAL APPLICATION WORKFLOW
function initModalWorkflows() {
    const modal = document.getElementById("application-modal");
    const btnClose = document.getElementById("btn-close-modal");
    const btnNext = document.getElementById("btn-next-step");
    const btnPrev = document.getElementById("btn-prev-step");
    const form = document.getElementById("service-app-form");

    btnClose.addEventListener("click", closeModal);
    btnNext.addEventListener("click", handleNextStep);
    btnPrev.addEventListener("click", handlePrevStep);

    // File Drag & Drop Simulation
    const dropzone = document.getElementById("file-dropzone");
    const fileInput = document.getElementById("app-file");
    const fileNameDisplay = document.getElementById("dz-file-name");

    dropzone.addEventListener("click", () => fileInput.click());
    fileInput.addEventListener("change", (e) => {
        if (e.target.files.length > 0) {
            fileNameDisplay.textContent = `Attached: ${e.target.files[0].name} (${(e.target.files[0].size / 1024 / 1024).toFixed(2)} MB) ✓`;
            document.getElementById("err-file").textContent = "";
        }
    });

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const decl = document.getElementById("app-declaration");
        if (!decl.checked) {
            document.getElementById("err-declaration").textContent = "You must confirm the legal accuracy statement.";
            return;
        }

        // Generate Submission Reference
        const randomRef = "GOV-2026-" + Math.floor(1000 + Math.random() * 9000);
        closeModal();
        
        // Populate tracking input automatically
        document.getElementById("track-id-input").value = randomRef;
        document.getElementById("btn-track-submit").click();

        showToast(`Application Submitted! Ref ID: ${randomRef}`);
        announceToScreenReader(`Application submitted successfully. Your reference code is ${randomRef}`);
    });
}

function openApplicationModal(srvId) {
    selectedService = SERVICES_DATA.find(s => s.id === srvId) || SERVICES_DATA[0];
    document.getElementById("modal-service-subtitle").textContent = selectedService.title;
    
    currentStep = 1;
    updateStepUI();
    document.getElementById("application-modal").classList.remove("hidden");
    document.getElementById("app-fullname").focus();
}

function closeModal() {
    document.getElementById("application-modal").classList.add("hidden");
}

function handleNextStep() {
    if (currentStep === 1) {
        // Validate Step 1 Fields
        const name = document.getElementById("app-fullname").value.trim();
        const idNum = document.getElementById("app-id").value.trim();
        const email = document.getElementById("app-email").value.trim();
        const phone = document.getElementById("app-phone").value.trim();

        let valid = true;
        if (!name) { document.getElementById("err-fullname").textContent = "Full Legal Name is required."; valid = false; }
        else { document.getElementById("err-fullname").textContent = ""; }

        if (!idNum) { document.getElementById("err-id").textContent = "National Citizen ID is required."; valid = false; }
        else { document.getElementById("err-id").textContent = ""; }

        if (!email.includes("@")) { document.getElementById("err-email").textContent = "Valid Email address is required."; valid = false; }
        else { document.getElementById("err-email").textContent = ""; }

        if (!phone) { document.getElementById("err-phone").textContent = "Phone number is required."; valid = false; }
        else { document.getElementById("err-phone").textContent = ""; }

        if (!valid) {
            announceToScreenReader("Form validation error. Please fill required fields.");
            return;
        }

        currentStep = 2;
    } else if (currentStep === 2) {
        // Step 2 validation (File Check)
        const fileInput = document.getElementById("app-file");
        if (fileInput.files.length === 0) {
            document.getElementById("err-file").textContent = "Please attach identification document scan.";
            return;
        }
        document.getElementById("err-file").textContent = "";

        // Populate Review Summary for Step 3
        document.getElementById("rev-name").textContent = document.getElementById("app-fullname").value;
        document.getElementById("rev-id").textContent = document.getElementById("app-id").value;
        document.getElementById("rev-email").textContent = document.getElementById("app-email").value;
        document.getElementById("rev-service").textContent = selectedService.title;

        currentStep = 3;
    }
    updateStepUI();
}

function handlePrevStep() {
    if (currentStep > 1) {
        currentStep--;
        updateStepUI();
    }
}

function updateStepUI() {
    // Hide all panels
    document.getElementById("step-panel-1").classList.add("hidden");
    document.getElementById("step-panel-2").classList.add("hidden");
    document.getElementById("step-panel-3").classList.add("hidden");

    // Stepper Tab Highlights
    document.querySelectorAll(".modal-step").forEach((tab, idx) => {
        if (idx + 1 === currentStep) tab.classList.add("active");
        else tab.classList.remove("active");
    });

    // Show current panel
    document.getElementById(`step-panel-${currentStep}`).classList.remove("hidden");

    // Button state logic
    const btnPrev = document.getElementById("btn-prev-step");
    const btnNext = document.getElementById("btn-next-step");
    const btnSubmit = document.getElementById("btn-submit-app");

    if (currentStep === 1) {
        btnPrev.classList.add("hidden");
        btnNext.classList.remove("hidden");
        btnNext.textContent = "Proceed to Step 2 ➔";
        btnSubmit.classList.add("hidden");
    } else if (currentStep === 2) {
        btnPrev.classList.remove("hidden");
        btnNext.classList.remove("hidden");
        btnNext.textContent = "Review & Finalize ➔";
        btnSubmit.classList.add("hidden");
    } else if (currentStep === 3) {
        btnPrev.classList.remove("hidden");
        btnNext.classList.add("hidden");
        btnSubmit.classList.remove("hidden");
    }
}

// 6. REAL-TIME TRACKING LOOKUP SYSTEM
function initTrackerSystem() {
    const btnSubmit = document.getElementById("btn-track-submit");
    const btnOpenTracker = document.getElementById("btn-open-tracker");
    const input = document.getElementById("track-id-input");
    const resultBox = document.getElementById("tracking-result");

    btnOpenTracker.addEventListener("click", () => {
        document.getElementById("tracking-section").scrollIntoView({ behavior: "smooth" });
        input.focus();
    });

    btnSubmit.addEventListener("click", () => {
        const query = input.value.trim().toUpperCase();
        if (!query) {
            showToast("Please enter a reference code (e.g. GOV-2026-8942)");
            return;
        }

        resultBox.classList.remove("hidden");
        document.getElementById("res-ref-code").textContent = query;
        showToast(`Tracking status retrieved for ${query}`);
        announceToScreenReader(`Tracking status loaded for ${query}. Current status: Identity Verification In Progress.`);
    });
}

// HELPER ANNOUNCER & TOAST
function showToast(message) {
    const toast = document.getElementById("toast-notification");
    toast.textContent = message;
    toast.classList.remove("hidden");
    setTimeout(() => toast.classList.add("hidden"), 3500);
}

function announceToScreenReader(message) {
    const announcer = document.getElementById("aria-announcer");
    announcer.textContent = message;
}
