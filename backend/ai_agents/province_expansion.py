# ai_agents/province_expansion.py
class ProvinceExpansionAI:
    def __init__(self):
        self.western_cape_model = self.load_western_cape_model()
        self.provinces = {
            'Gauteng': {'status': 'active', 'progress': 95},
            'KwaZulu-Natal': {'status': 'active', 'progress': 85},
            'Eastern Cape': {'status': 'active', 'progress': 75},
            'Free State': {'status': 'active', 'progress': 70},
            'Limpopo': {'status': 'active', 'progress': 65},
            'Mpumalanga': {'status': 'active', 'progress': 60},
            'North West': {'status': 'active', 'progress': 55},
            'Northern Cape': {'status': 'active', 'progress': 50}
        }
        
    def expand_to_all_provinces(self):
        """Automatically expand to all provinces using Western Cape model"""
        for province, data in self.provinces.items():
            if data['progress'] < 100:
                self.expand_to_province(province)
                
    def expand_to_province(self, province):
        """Expand to a specific province"""
        print(f"Expanding to {province}...")
        
        # Create regions based on Western Cape model
        regions = self.create_regions_for_province(province)
        
        # Create towns for each region
        for region in regions:
            towns = self.create_towns_for_region(region, province)
            self.add_towns_to_database(towns)
            
        # Update progress
        self.provinces[province]['progress'] = 100
        self.provinces[province]['status'] = 'completed'
        
        print(f"Successfully expanded to {province} with {len(regions)} regions")
        
    def create_regions_for_province(self, province):
        """Create regions for a province based on its geography"""
        region_templates = {
            'Gauteng': ['Johannesburg Metro', 'Pretoria Region', 'East Rand', 'West Rand', 'Vaal Triangle'],
            'KwaZulu-Natal': ['Durban Metro', 'North Coast', 'South Coast', 'Midlands', 'Zululand'],
            'Eastern Cape': ['Nelson Mandela Bay', 'Buffalo City', 'Wild Coast', 'Karoo Region', 'Sunshine Coast'],
            'Free State': ['Bloemfontein Central', 'Northern Free State', 'Eastern Free State', 'Southern Free State'],
            'Limpopo': ['Polokwane Region', 'Waterberg', 'Vhembe', 'Capricorn', 'Mopani'],
            'Mpumalanga': ['Mbombela Region', 'Highveld', 'Lowveld', 'Kruger Region'],
            'North West': ['Rustenburg Region', 'Potchefstroom Area', 'Klerksdorp Area', 'Madibeng'],
            'Northern Cape': ['Kimberley Region', 'Kalahari', 'Karoo', 'Namaqualand', 'Green Kalahari']
        }
        
        return region_templates.get(province, [])
