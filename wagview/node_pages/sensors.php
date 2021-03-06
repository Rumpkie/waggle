<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">

		<title>Array of Things @ University of Chicago, Regenstein Library</title>

		<!-- Grab necessary Bootstrap, JavaScript, JQuery, and styles -->
		<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
		<link rel="stylesheet" href="style.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
		<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script>
		<script src="update.js"></script>
		<script src="parse.js"></script>
		<script src="graph.js"></script>
		<script src="page_id.js"></script>
		<script src="configs.js"></script>

		<!-- Start the timer to update the webpage -->
		<script>	
	//		timer();
		</script>
	</head>

	<body>
		<!-- Top area -->
		<div class="container=fluid" id="header">
			<div class="row" style="margin: auto">
				<div class="col-md-12" style="color: #fff">
					<h3 id="org_loc_pos_data"></h3>
				</div>
			</div>
			<div class="row" style="margin: auto">
				<div class="col-md-6" style="color: #fff">
					<h4 id="coordinates"></h4>
				</div>
				<div class="col-md-6" style="color: #fff">
					<h4 id="installed"></h4>
				</div>
			</div>
			<div class="row">
				<div class="col-md-12" id="banner">
				</div>
			</div>
			<div class="row">
				<div class="col-md-3" style="position: relative; left: 2.5%">
					<h3 id="date"><h3>
				</div>
			</div>
		</div>

		<!-- Sensor data -->
		<!-- Container is broken into 12 segments, each div takes up a certain amount of segments, and fills the space up going from right to left,
			 top to bottom. If a div element will push past the 12 segments, it moves down a row to the next open space -->
		<div class="container-fluid" id="data_container">
			<div class="col-md-4" style="height: 60px">
				<p><strong>RHT03</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="RHT03_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph00"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>SHT15</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="SHT15_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph10"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>SHT75</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="SHT75_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph20"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Humidity</p><p id="RHT03_hum" style="width: 50%; float: left">%RH</p></div>
				<div class="col-md-6" id="graph01"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Humidity</p><p id="SHT15_hum" style="width: 50%; float: left">%RH</p></div>
				<div class="col-md-6" id="graph11"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Humidity</p><p id="SHT75_hum" style="width: 50%; float: left">%RH</p></div>
				<div class="col-md-6" id="graph21"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>HTU21D</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="HTU21D_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph02"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>D6T44L06</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Avg. Temperature</p><p id="D6T44L06_avg_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph12"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>BMP180</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="BMP180_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph22"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Humidity</p><p id="HTU21D_hum" style="width: 50%; float: left">%RH</p></div>
				<div class="col-md-6" id="graph03"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
				<div class="col-md-6"><p style="width: 58%; float: left">Casing Temperature&nbsp</p><p id="D6T44L06_case_temp" style="width: 42%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph13"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Pressure</p><p id="BMP180_pres" style="width: 50%; float: left">hPa</p></div>
				<div class="col-md-6" id="graph23"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>HIH6130</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="HIH6130_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph04"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>HIH4030</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Humidity</p><p id="HIH4030" style="width: 50%; float: left">%RH</p></div>
				<div class="col-md-6" id="graph14"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>DS18B20</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="DS18B20" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph24"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Humidity</p><p id="HIH6130_hum" style="width: 50%; float: left">%RH</p></div>
				<div class="col-md-6" id="graph05"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>TMP102</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="TMP102" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph15"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>TMP421</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="TMP421" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph25"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>MLX90614ESF</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="MLX90614ESF" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph06"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>PR103J2</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="PR103J2" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph16"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>GA1A1S201WP</strong></p>
				<div class="col-md-6"><p style="width: 56%; float: left">Luminous Intensity&nbsp</p><p id="GA1A1S201WP" style="width: 44%; float: left">raw A/D</p></div>
				<div class="col-md-6" id="graph26"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>MMA8452Q</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Acceleration x</p><p id="MMA8452Q_x" style="width: 50%; float: left">g</p></div>
				<div class="col-md-6" id="graph07"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>HMC5883</strong></p>
				<div class="col-md-6"><p style="width: 58%; float: left">Magnetic Field x</p><p id="HMC5883_x" style="width: 42%; float: left">&microT</p></div>
				<div class="col-md-6" id="graph17"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>PDVP8104</strong></p>
				<div class="col-md-6"><p style="width: 56%; float: left">Luminous Intensity&nbsp</p><p id="PDVP8104" style="width: 44%; float: left">raw A/D</p></div>
				<div class="col-md-6" id="graph27"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Accleration y</p><p id="MMA8452Q_y" style="width: 50%; float: left">g</p></div>
				<div class="col-md-6" id="graph08"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
				<div class="col-md-6"><p style="width: 58%; float: left">Magnetic Field y</p><p id="HMC5883_y" style="width: 42%; float: left">&microT</p></div>
				<div class="col-md-6" id="graph18"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>MAX4466</strong></p>
				<div class="col-md-6"><p style="width: 56%; float: left">Acoustic Intensity</p><p id="MAX4466" style="width: 44%; float: left">raw A/D</p></div>
				<div class="col-md-6" id="graph28"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Acceleration z</p><p id="MMA8452Q_z" style="width: 50%; float: left">g</p></div>
				<div class="col-md-6" id="graph09"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
				<div class="col-md-6"><p style="width: 58%; float: left">Magnetic Field z</p><p id="HMC5883_z" style="width: 42%; float: left">&microT</p></div>
				<div class="col-md-6" id="graph19"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>&nbsp</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">RMS Vibration</p><p id="MMA8452Q_rms" style="width: 50%; float: left">g</p></div>
				<div class="col-md-6" id="graph010"></div>
			</div>


		<!--<div class="container-fluid" id="data_container">
			<div class="col-md-4" style="height: 120px">
				<p><strong>RHT03</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="RHT03_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph000"></div>
				<div class="col-md-6"><p style="width: 50%; float: left">Humidity</p><p id="RHT03_hum" style="width: 50%; float: left">%RH</p></div>
				<div class="col-md-6" id="graph001"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>DS18B20</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="DS18B20" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph10"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong>Total Reducing Gases</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">-</p><p id="ReducingGases" style="width: 50%; float: left">-</p></div>
				<div class="col-md-6" id="graph20"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>GA1A1S201WP</strong></p>
				<div class="col-md-6"><p style="width: 56%; float: left">Luminous Intensity&nbsp</p><p id="GA1A1S201WP" style="width: 44%; float: left">raw A/D</p></div>
				<div class="col-md-6" id="graph11"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>Ethanol</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">-</p><p id="Ethanol" style="width: 50%; float: left">-</p></div>
				<div class="col-md-6" id="graph21"></div>
			</div>
			<div class="col-md-4" style="height: 120px">
				<div id="divide"></div>
				<p><strong>SHT15</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="SHT15_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph010"></div>
				<div class="col-md-6"><p style="width: 50%; float: left">Humidity</p><p id="SHT15_hum" style="width: 50%; float: left">%RH</p></div>
				<div class="col-md-6" id="graph011"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>PDVP8104</strong></p>
				<div class="col-md-6"><p style="width: 56%; float: left">Luminous Intensity&nbsp</p><p id="PDVP8104" style="width: 44%; float: left">raw A/D</p></div>
				<div class="col-md-6" id="graph12"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>Nitrogen</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">-</p><p id="Nitrogen" style="width: 50%; float: left">-</p></div>
				<div class="col-md-6" id="graph22"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>MAX4466</strong></p>
				<div class="col-md-6"><p style="width: 56%; float: left">Acoustic Intensity</p><p id="MAX4466" style="width: 44%; float: left">raw A/D</p></div>
				<div class="col-md-6" id="graph13"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>Ozone</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">-</p><p id="Ozone" style="width: 50%; float: left">-</p></div>
				<div class="col-md-6" id="graph23"></div>
			</div>
			<div class="col-md-4" style="height: 120px">
				<div id="divide"></div>
				<p><strong>SHT75</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="SHT75_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph020"></div>
				<div class="col-md-6"><p style="width: 50%; float: left">Humidity</p><p id="SHT75_hum" style="width: 50%; float: left">%RH</p></div>
				<div class="col-md-6" id="graph021"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>MLX90614ESF</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="MLX90614ESF" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph14"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>Hydrogen Sulphide</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">-</p><p id="HydrogenSulphide" style="width: 50%; float: left">-</p></div>
				<div class="col-md-6" id="graph24"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>PR103J2</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="PR103J2" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph15"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>Total Oxidizing Gases</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">-</p><p id="OxidizingGases" style="width: 50%; float: left">-</p></div>
				<div class="col-md-6" id="graph25"></div>
			</div>
			<div class="col-md-4" style="height: 180px">
				<div id="divide"></div>
				<p><strong>HMC5883</strong></p>
				<div class="col-md-6"><p style="width: 58%; float: left">Magnetic Field x</p><p id="HMC5883_x" style="width: 42%; float: left">&microT</p></div>
				<div class="col-md-6" id="graph030"></div>
				<div class="col-md-6"><p style="width: 58%; float: left">Magnetic Field y</p><p id="HMC5883_y" style="width: 42%; float: left">&microT</p></div>
				<div class="col-md-6" id="graph031"></div>
				<div class="col-md-6"><p style="width: 58%; float: left">Magnetic Field z</p><p id="HMC5883_z" style="width: 42%; float: left">&microT</p></div>
				<div class="col-md-6" id="graph032"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>TMP102</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="TMP102" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph16"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>Carbon Monoxide</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">-</p><p id="CarbonMonoxide" style="width: 50%; float: left">-</p></div>
				<div class="col-md-6" id="graph26"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>TMP421</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="TMP421" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph17"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>Sulphur Dioxide</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">-</p><p id="SulphurDioxide" style="width: 50%; float: left">-</p></div>
				<div class="col-md-6" id="graph27"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<div id="divide"></div>
				<p><strong>HIH4030</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Humidity</p><p id="HIH4030" style="width: 50%; float: left">%RH</p></div>
				<div class="col-md-6" id="graph18"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong></strong></p>
			</div>
			<div class="col-md-4" style="height: 120px">
				<div id="divide"></div>
				<p><strong>BMP180</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="BMP180_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph040"></div>
				<div class="col-md-6"><p style="width: 50%; float: left">Pressure</p><p id="BMP180_pres"style="width: 50%; float: left">hPa</p></div>
				<div class="col-md-6" id="graph041"></div>
			</div>
			<div class="col-md-4" style="height: 120px">
				<div id="divide"></div>
				<p><strong>HIH6130</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="HIH6130_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph190"></div>
				<div class="col-md-6"><p style="width: 50%; float: left">Humidity</p><p id="HIH6130_hum" style="width: 50%; float: left">%RH</p></div>
				<div class="col-md-6" id="graph191"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong></strong></p>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong></strong></p>
			</div>
			<div class="col-md-4" style="height: 240px">
				<div id="divide"></div>
				<p><strong>MMA8452Q</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Acceleration x</p><p id="MMA8452Q_x" style="width: 50%; float: left">g</p></div>
				<div class="col-md-6" id="graph050"></div>
				<div class="col-md-6"><p style="width: 50%; float: left">Acceleration y</p><p id="MMA8452Q_y" style="width: 50%; float: left">g</p></div>
				<div class="col-md-6" id="graph051"></div>
				<div class="col-md-6"><p style="width: 50%; float: left">Acceleration z</p><p id="MMA8452Q_z" style="width: 50%; float: left">g</p></div>
				<div class="col-md-6" id="graph052"></div>
				<div class="col-md-6"><p style="width: 50%; float: left">RMS Vibration</p><p id="MMA8452Q_rms" style="width: 50%; float: left">g</p></div>
				<div class="col-md-6" id="graph053"></div>
			</div>
			<div class="col-md-4" style="height: 120px">
				<div id="divide"></div>
				<p><strong>HTU21D</strong></p>
				<div class="col-md-6"><p style="width: 50%; float: left">Temperature</p><p id="HTU21D_temp" style="width: 50%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph1100"></div>
				<div class="col-md-6"><p style="width: 50%; float: left">Humidity</p><p id="HTU21D_hum" style="width: 50%; float: left">%RH</p></div>
				<div class="col-md-6" id="graph1101"></div>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong></strong></p>
			</div>
			<div class="col-md-4" style="height: 60px">
				<p><strong></strong></p>
			</div>
			<div class="col-md-4" style="height: 120px">
				<div id="divide"></div>
				<p><strong>D6T44L06</strong></p>
				<div class="col-md-6"><p style="width: 55%; float: left">Avg. Temperature</p><p id="D6T44L06_avg_temp" style="width: 45%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph1110"></div>
				<div class="col-md-6"><p style="width: 60%; float: left">Casing Temperature</p><p id="D6T44L06_case_temp" style="width: 40%; float: left">&degC</p></div>
				<div class="col-md-6" id="graph1111"></div>
			</div>-->
		</div>
		<script>
			<?php
				$str = $_GET['name'];
			?>
			var search_str = "<?php echo $str; ?>";
			load_customized_data(search_str);
		</script>
	</body>
</html>
