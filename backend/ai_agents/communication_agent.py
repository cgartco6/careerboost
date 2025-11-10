# ai_agents/communication_agent.py
class CommunicationAgent:
    def __init__(self):
        self.email_templates = self.load_email_templates()
        self.sms_templates = self.load_sms_templates()
        self.review_requests_sent = 0
        self.testimonials_collected = 0
        
    def maintain_customer_relationships(self):
        """Maintain regular contact with all customers"""
        customers = self.get_active_customers()
        
        for customer in customers:
            # Send personalized check-ins
            self.send_personalized_checkin(customer)
            
            # Request reviews after successful hires
            if customer.hired and not customer.review_requested:
                self.request_review(customer)
                
            # Gather testimonials
            if customer.hired and customer.satisfaction_score >= 4:
                self.request_testimonial(customer)
                
            # Send career tips and market insights
            self.send_career_insights(customer)
    
    def request_review(self, customer):
        """Send review request to customer"""
        template = self.email_templates['review_request']
        personalized_email = self.personalize_template(template, customer)
        
        self.send_email(customer.email, "How was your CareerBoost experience?", personalized_email)
        self.review_requests_sent += 1
        customer.review_requested = True
        customer.save()
        
    def request_testimonial(self, customer):
        """Request testimonial from satisfied customer"""
        template = self.email_templates['testimonial_request']
        personalized_email = self.personalize_template(template, customer)
        
        # Offer incentive for testimonial
        incentive = "R100 voucher"
        
        self.send_email(customer.email, "Share your success story!", personalized_email)
        self.testimonials_collected += 1
