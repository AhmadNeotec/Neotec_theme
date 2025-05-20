// apps/neotec_theme/neotec_theme/public/js/theme.js
frappe.ui.ThemeSwitcher = class CustomThemeSwitcher extends frappe.ui.ThemeSwitcher {
    constructor() {
        super();
        console.log("Theme JS initialized");
        this.apply_saved_theme();
    }

    fetch_themes() {
        return new Promise((resolve) => {
            this.themes = [
                { name: "Light", label: "Frappe Light", info: "Light Theme" },
                { name: "Dark", label: "Timeless Night", info: "Dark Theme" },
                { name: "Alphax Theme", label: "Alphax Theme", info: "Custom Neotec theme" },
                { name: "Automatic", label: "Automatic", info: "Uses system's theme" },
            ];
            resolve(this.themes);
        });
    }

    apply_saved_theme() {
        console.log("Theme JS loaded");
        frappe.call({
            method: "frappe.client.get_value",
            args: {
                doctype: "User",
                filters: { name: frappe.session.user },
                fieldname: "desk_theme"
            },
            callback: (response) => {
                const saved_theme = response.message?.desk_theme || "Alphax Theme";
                console.log("Applying saved theme:", saved_theme);
                this.switch(saved_theme);
            },
            error: (err) => {
                console.error("Error fetching theme:", err);
                this.switch("Alphax Theme");
            }
        });
    }

    switch(theme) {
        console.log("Switching to:", theme);
        frappe.call({
            method: "frappe.core.doctype.user.user.switch_theme",
            args: { theme: theme },
            callback: () => console.log("Theme switch successful:", theme),
            error: (err) => console.error("Theme switch error:", err)
        });
        if (super.switch) {
            super.switch(theme);
        }
        document.documentElement.setAttribute("data-theme", theme.toLowerCase().replace(" ", "_"));
    }
}