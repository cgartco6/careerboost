# ai_agents/payout_agent.py
class PayoutAgent:
    def __init__(self):
        self.fnb_client = FNBClient()
        self.african_bank_client = AfricanBankClient()
        self.distribution = {
            'owner_fnb': 0.4,      # 40%
            'owner_african_bank': 0.2,  # 20%
            'reserve_fnb': 0.2,    # 20%
            'ai_development': 0.2   # 20%
        }
        
    def process_weekly_payouts(self):
        """Process weekly revenue distribution"""
        weekly_revenue = self.calculate_weekly_revenue()
        
        distributions = {}
        for account, percentage in self.distribution.items():
            amount = weekly_revenue * percentage
            distributions[account] = amount
            
        # Execute transfers
        self.transfer_to_owner_fnb(distributions['owner_fnb'])
        self.transfer_to_african_bank(distributions['owner_african_bank'])
        self.transfer_to_reserve(distributions['reserve_fnb'])
        self.transfer_to_ai_development(distributions['ai_development'])
        
        # Log payout transaction
        self.log_payout_transaction(weekly_revenue, distributions)
        
        return distributions
    
    def transfer_to_owner_fnb(self, amount):
        """Transfer to owner's FNB account"""
        self.fnb_client.transfer(
            amount=amount,
            to_account=os.getenv('OWNER_FNB_ACCOUNT'),
            reference=f"CareerBoost Payout {datetime.now().strftime('%Y-%m-%d')}"
        )
        
    def transfer_to_african_bank(self, amount):
        """Transfer to owner's African Bank account"""
        self.african_bank_client.transfer(
            amount=amount,
            to_account=os.getenv('OWNER_AFRICAN_BANK_ACCOUNT'),
            reference=f"CareerBoost Payout {datetime.now().strftime('%Y-%m-%d')}"
        )
