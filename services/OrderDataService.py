from orders.models import UserSteps, TradelineOrder


class OrderDataService:

    @classmethod
    def get_user_steps_data(cls, user):
        user_steps = UserSteps.objects.filter(user=user)
        services = []
        for i in user_steps:
            for k in ['website', 'toll_free_number',
                      'fax_number',
                      'domain',
                      'professional_email_address']:
                status = getattr(i, k)
                if status == 2 or status == 3:
                    dash = ''
                    if k == 'website':
                        dash = "/business/website-creation-paid"
                    elif k == 'toll_free_number':
                        dash = '/business/toll-free-options/'
                    elif k == 'fax_number':
                        dash = "/business/fax-number-paid"
                    elif k == 'domain':
                        dash = getattr(i, 'domain_dashboard')
                    elif k == 'professional_email_address':
                        dash = getattr(i, 'email_provider')
                    serv = {
                        'name': k.replace('_', " "),
                        'status': 'Done' if status == 3 else 'In progress',
                        'product': getattr(i, k + '_act'),
                        'dashboard': dash
                    }
                    services.append(serv)
        return services

    @classmethod
    def get_user_tradelines_data(cls, user):
        tradelines = TradelineOrder.objects.filter(user=user)
        tradeline_data = []

        for tradeline in tradelines:
            data = {
                'name': tradeline.tradeline.company_name,
                'product': tradeline.tradeline.product,
                'amount': float(tradeline.tradeline.tradeline_amount),
                'price': float(tradeline.tradeline.price),
                'charge': float(tradeline.tradeline.charge),
            }
            tradeline_data.append(data)
        return tradeline_data
