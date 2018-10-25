params = 0.001, 1, 9.81, 3, 0.57, 0.35, 46*(10**6), 0.832



def FuelConsumption(V, t, M, theta, params) :
    mu, rho, g, A, Cp, eta, H, densDiesel = params                               # Constants are extracted via params
    N = len(V)                                                                   # FC (will be calculated in L/tonnes)
    FC1 = [[round((((mu)*(M[i][j])*(1000)*(g)*(math.cos(theta[i][j]))+(M[i][j])*(1000)*(g)*(math.sin(theta[i][j]))+0.5*(rho)*(Cp)*(A)*((V[i][j])**2))*((V[i][j]))*(t[i][j]*60))/(eta*H*(densDiesel)),3) for i in range(N)] for j in range(N)]
	
    return FC1

def FuelConsumptionStoD(V, t, Mc, theta, params) :
    mu, rho, g, A, Cp, eta, H, densDiesel = params                               # Constants are extracted via params
    N = len(V)                                                                   # FC (will be calculated in L/tonnes)
    FC2 = [round((((mu)*(Mc)*(1000)*(g)*(math.cos(theta[i]))+(Mc)*(1000)*(g)*(math.sin(theta[i]))+0.5*(rho)*(Cp)*(A)*((V[i])**2))*((V[i]))*(t[i]*60))/(eta*H*(densDiesel)),3) for i in range(N)]
	
    return FC2