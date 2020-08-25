import json

from DiseaseAlgorithm.DiseaseType import DiseaseType

class DiseaseManager:

    def __init__(self):
        self.diseases = self.import_diseases()


    def import_diseases(self):
        diseases = {}

        with open('./Settings/diseases.json', mode='r') as in_file:
            data = json.load(in_file)

            for disease_name, disease_stats in data.items():
                diseases[disease_name] = DiseaseType(
                    name=disease_stats['name'],
                    diagnose_days=disease_stats['diagnose_days'],
                    recovery_days=disease_stats['recovery_days'],
                    infection_chance=disease_stats['infection_chance'],
                    re_infection_chance=disease_stats['re_infection_chance'],
                    fatality_chance=disease_stats['fatality_chance'],
                )

        return diseases



    def create(self, name, diagnose_days, recovery_days, infection_chance, re_infection_chance, fatality_chance):
        if name not in self.diseases:
            self.diseases[f'{name}'] = DiseaseType(name, infection_chance, re_infection_chance, fatality_chance, diagnose_days, recovery_days)

        self.export_diseases()


    def export_diseases(self):
        all_diseases = {disease_name: disease_type.dict() for disease_name, disease_type in self.diseases.items()}

        with open('./Settings/diseases.json', mode='w') as out_file:
            json.dump(all_diseases, out_file)