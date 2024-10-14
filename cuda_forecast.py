def cuda_forecast_model(location):
   
    if not torch.cuda.is_available():
        return "CUDA not available on this system"

    try:
        device = torch.device("cuda")
        
       
        model = SolarForecastModel().to(device)
        inputs = torch.randn(10).to(device)
        
       
        model.eval()
        with torch.no_grad():
            prediction = model(inputs)
        
        return round(prediction.item(), 2)
    
    except Exception as e:
        return f"Error during model inference: {str(e)}"
