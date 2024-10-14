<div class="demo-container">
    <h2 style="text-align: center;">Try Our AI-Powered Solar Forecasting Tool</h2>

    <form id="forecastForm">
        <label for="location">Enter Your Location:</label>
        <input type="text" id="location" name="location" required placeholder="City, Country" style="padding: 10px; font-size: 16px;">
        <button type="submit" id="getForecastBtn" >Get Solar Forecast</button>
    </form>

    <div id="forecastResult" class="hidden">
        <h3>Solar Energy Forecast</h3>
        <p id="forecastOutput"></p>
        <canvas id="forecastChart"></canvas>
    </div>
</div>


