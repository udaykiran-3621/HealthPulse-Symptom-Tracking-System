import customtkinter as ctk
from storage import load, save
from datetime import date

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class HealthPulseApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("HealthPulse - Symptom Tracking System")
        self.geometry("1100x700")
        self.minsize(900, 550)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        ctk.CTkLabel(
            self.sidebar,
            text="❤ HealthPulse",
            font=("Arial", 25, "bold")
        ).pack(pady=35)

        buttons = [
            ("Dashboard", self.show_dashboard),
            ("Add Patient", self.add_patient),
            ("Add Symptom", self.add_symptom),
            ("View Patients", self.view_patients),
            ("View Symptoms", self.view_symptoms),
            ("Reports", self.show_reports)
        ]

        for name, command in buttons:
            ctk.CTkButton(
                self.sidebar,
                text=name,
                height=40,
                command=command
            ).pack(fill="x", padx=15, pady=8)

        ctk.CTkButton(
            self.sidebar,
            text="Exit",
            fg_color="red",
            hover_color="#990000",
            command=self.destroy
        ).pack(side="bottom", fill="x", padx=15, pady=25)

        # Main Content
        self.content = ctk.CTkFrame(self, corner_radius=0)
        self.content.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )

        self.show_dashboard()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # ---------------- Dashboard ----------------

    def show_dashboard(self):
        self.clear_content()

        patients = load("data/patients.json")
        symptoms = load("data/symptoms.json")

        ctk.CTkLabel(
            self.content,
            text="Welcome to HealthPulse",
            font=("Arial", 30, "bold")
        ).pack(pady=40)

        ctk.CTkLabel(
            self.content,
            text="Patient and Symptom Tracking System",
            font=("Arial", 18)
        ).pack()

        cards = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )
        cards.pack(pady=40)

        patient_card = ctk.CTkFrame(
            cards,
            width=250,
            height=150
        )
        patient_card.grid(row=0, column=0, padx=20)

        patient_card.pack_propagate(False)

        ctk.CTkLabel(
            patient_card,
            text="Total Patients",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            patient_card,
            text=str(len(patients)),
            font=("Arial", 35)
        ).pack()

        symptom_card = ctk.CTkFrame(
            cards,
            width=250,
            height=150
        )
        symptom_card.grid(row=0, column=1, padx=20)

        symptom_card.pack_propagate(False)

        ctk.CTkLabel(
            symptom_card,
            text="Total Symptoms",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            symptom_card,
            text=str(len(symptoms)),
            font=("Arial", 35)
        ).pack()
    
    # ---------------- Add Patient ----------------

    def add_patient(self):
        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="Add New Patient",
            font=("Arial", 28, "bold")
        ).pack(pady=30)

        patient_id = ctk.CTkEntry(
            self.content,
            placeholder_text="Enter Patient ID",
            width=350
        )
        patient_id.pack(pady=10)

        patient_name = ctk.CTkEntry(
            self.content,
            placeholder_text="Enter Patient Name",
            width=350
        )
        patient_name.pack(pady=10)

        patient_age = ctk.CTkEntry(
            self.content,
            placeholder_text="Enter Age",
            width=350
        )
        patient_age.pack(pady=10)

        message = ctk.CTkLabel(
            self.content,
            text=""
        )
        message.pack(pady=10)

        def save_patient():

            pid = patient_id.get().strip()
            name = patient_name.get().strip()
            age = patient_age.get().strip()

            if pid == "" or name == "" or age == "":
                message.configure(
                    text="Please fill all fields!",
                    text_color="red"
                )
                return

            patients = load("data/patients.json")

            for patient in patients:
                if patient["id"] == pid:
                    message.configure(
                        text="Patient ID already exists!",
                        text_color="red"
                    )
                    return

            patients.append({
                "id": pid,
                "name": name,
                "age": age
            })

            save("data/patients.json", patients)

            message.configure(
                text="Patient Added Successfully!",
                text_color="green"
            )

            patient_id.delete(0, "end")
            patient_name.delete(0, "end")
            patient_age.delete(0, "end")

        ctk.CTkButton(
            self.content,
            text="Save Patient",
            width=180,
            command=save_patient
        ).pack(pady=20)

    # ---------------- View Patients ----------------

    def view_patients(self):
        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="Patient Records",
            font=("Arial", 28, "bold")
        ).pack(pady=25)

        patients = load("data/patients.json")

        table = ctk.CTkScrollableFrame(
            self.content,
            width=750,
            height=420
        )

        table.pack(pady=10)

        headers = [
            "Patient ID",
            "Patient Name",
            "Age"
        ]

        for col, header in enumerate(headers):

            ctk.CTkLabel(
                table,
                text=header,
                width=200,
                font=("Arial", 16, "bold")
            ).grid(
                row=0,
                column=col,
                padx=10,
                pady=10
            )

        for row, patient in enumerate(patients, start=1):

            ctk.CTkLabel(
                table,
                text=patient["id"],
                width=200
            ).grid(row=row, column=0, pady=8)

            ctk.CTkLabel(
                table,
                text=patient["name"],
                width=200
            ).grid(row=row, column=1, pady=8)

            ctk.CTkLabel(
                table,
                text=patient["age"],
                width=200
            ).grid(row=row, column=2, pady=8)

        if len(patients) == 0:
            ctk.CTkLabel(
                self.content,
                text="No Patient Records Found",
                font=("Arial", 16)
            ).pack(pady=20)

        # ---------------- Add Symptom ----------------

    def add_symptom(self):
        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="Add New Symptom",
            font=("Arial", 28, "bold")
        ).pack(pady=30)

        patients = load("data/patients.json")

        if len(patients) == 0:
            ctk.CTkLabel(
                self.content,
                text="No Patients Available!\nPlease Add a Patient First.",
                font=("Arial", 18),
                text_color="red"
            ).pack(pady=30)
            return

        patient_ids = [p["id"] for p in patients]

        patient = ctk.CTkComboBox(
            self.content,
            values=patient_ids,
            width=350
        )
        patient.pack(pady=10)
        patient.set(patient_ids[0])

        symptom = ctk.CTkEntry(
            self.content,
            placeholder_text="Enter Symptom",
            width=350
        )
        symptom.pack(pady=10)

        severity = ctk.CTkComboBox(
            self.content,
            values=["Low", "Medium", "High"],
            width=350
        )
        severity.pack(pady=10)
        severity.set("Low")

        symptom_date = ctk.CTkEntry(
            self.content,
            width=350
        )
        symptom_date.pack(pady=10)
        symptom_date.insert(0, date.today().strftime("%Y-%m-%d"))

        message = ctk.CTkLabel(self.content, text="")
        message.pack(pady=10)

        def save_symptom():

            symptoms = load("data/symptoms.json")

            symptoms.append({
                "patient": patient.get(),
                "symptom": symptom.get(),
                "severity": severity.get(),
                "date": symptom_date.get()
            })

            save("data/symptoms.json", symptoms)

            message.configure(
                text="Symptom Saved Successfully!",
                text_color="green"
            )

            symptom.delete(0, "end")

        ctk.CTkButton(
            self.content,
            text="Save Symptom",
            width=180,
            command=save_symptom
        ).pack(pady=20)

    # ---------------- View Symptoms ----------------

    def view_symptoms(self):
        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="Symptom Records",
            font=("Arial", 28, "bold")
        ).pack(pady=25)

        symptoms = load("data/symptoms.json")

        table = ctk.CTkScrollableFrame(
            self.content,
            width=850,
            height=420
        )
        table.pack(pady=10)

        headers = [
            "Patient ID",
            "Symptom",
            "Severity",
            "Date"
        ]

        for col, header in enumerate(headers):

            ctk.CTkLabel(
                table,
                text=header,
                width=180,
                font=("Arial", 16, "bold")
            ).grid(
                row=0,
                column=col,
                padx=10,
                pady=10
            )

        for row, s in enumerate(symptoms, start=1):

            ctk.CTkLabel(
                table,
                text=s["patient"],
                width=180
            ).grid(row=row, column=0)

            ctk.CTkLabel(
                table,
                text=s["symptom"],
                width=180
            ).grid(row=row, column=1)

            ctk.CTkLabel(
                table,
                text=s["severity"],
                width=180
            ).grid(row=row, column=2)

            ctk.CTkLabel(
                table,
                text=s["date"],
                width=180
            ).grid(row=row, column=3)

        if len(symptoms) == 0:
            ctk.CTkLabel(
                self.content,
                text="No Symptom Records Found",
                font=("Arial", 16)
            ).pack(pady=20)

        # ---------------- Reports ----------------

    def show_reports(self):
        self.clear_content()

        patients = load("data/patients.json")
        symptoms = load("data/symptoms.json")

        ctk.CTkLabel(
            self.content,
            text="HealthPulse Reports",
            font=("Arial", 30, "bold")
        ).pack(pady=30)

        report_frame = ctk.CTkFrame(self.content)
        report_frame.pack(pady=20)

        ctk.CTkLabel(
            report_frame,
            text=f"Total Patients : {len(patients)}",
            font=("Arial", 20)
        ).pack(pady=15)

        ctk.CTkLabel(
            report_frame,
            text=f"Total Symptoms : {len(symptoms)}",
            font=("Arial", 20)
        ).pack(pady=15)

        severity_count = {
            "Low": 0,
            "Medium": 0,
            "High": 0
        }

        for symptom in symptoms:
            level = symptom.get("severity", "Low")
            if level in severity_count:
                severity_count[level] += 1

        ctk.CTkLabel(
            report_frame,
            text=f"Low Severity : {severity_count['Low']}",
            font=("Arial", 18)
        ).pack(pady=8)

        ctk.CTkLabel(
            report_frame,
            text=f"Medium Severity : {severity_count['Medium']}",
            font=("Arial", 18)
        ).pack(pady=8)

        ctk.CTkLabel(
            report_frame,
            text=f"High Severity : {severity_count['High']}",
            font=("Arial", 18)
        ).pack(pady=8)


if __name__ == "__main__":
    app = HealthPulseApp()
    app.mainloop()