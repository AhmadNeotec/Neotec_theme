// apps/neotec_theme/neotec_theme/public/js/theme.js
frappe.ui.ThemeSwitcher = class CustomThemeSwitcher extends frappe.ui.ThemeSwitcher {
    constructor() {
        super();
        this.apply_saved_theme(); // Apply theme on init
    }

    fetch_themes() {
        return new Promise((resolve) => {
            this.themes = [
                { name: "light", label: "Frappe Light", info: "Light Theme" },
                { name: "dark", label: "Timeless Night", info: "Dark Theme" },
                { name: "alphax_theme", label: "Alphax Theme", info: "The theme I copied from github" },
                { name: "automatic", label: "Automatic", info: "Uses system's theme" },
            ];
            resolve(this.themes);
        });
    }

    apply_saved_theme() {
        frappe.call({
            method: "frappe.client.get_value",
            args: {
                doctype: "User",
                filters: { name: frappe.session.user },
                fieldname: "desk_theme"
            },
            callback: (response) => {
                const saved_theme = response.message?.desk_theme || "alphax_theme"; // Fallback to alphax_theme
                console.log("Applying saved theme:", saved_theme); // Debug
                this.switch(saved_theme);
            },
            error: (err) => {
                console.error("Error fetching theme:", err);
            }
        });
    }

    switch(theme) {
		console.log("Switching to:", theme);
		frappe.call({
			method: "frappe.core.doctype.user.user.switch_theme",  // This should be overridden
			args: { theme: theme },
			callback: () => console.log("Theme switch successful:", theme),
			error: (err) => console.error("Theme switch error:", err)
		});
		super.switch(theme);
		if (theme === "alphax_theme") {
			document.documentElement.setAttribute("data-theme", "alphax_theme");
		}
	}
}