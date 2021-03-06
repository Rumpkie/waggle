/**
 ** /coresensors/v3/pbay/reintegrated
 ** sensor_setup.ino V3 (pbay)
 **/

void initializeSensorBoard()
{
    byte i;

    pinMode(PIN_SPV_AMP,INPUT);         // MODE ON?????????? WHERE????????????? HOW???????????? WHEN???????????
    pinMode(PIN_SVP_SPL,INPUT);
    pinMode(PIN_RAW_MIC,INPUT);
    pinMode(PIN_CHEMSENSE_POW, OUTPUT); // ON/OFF sensor, OUTPUT:LOW = ON
    digitalWrite(PIN_CHEMSENSE_POW, HIGH); // Power OFF the Chemsense board

    if (ds2401.reset() == TRUE)
    {
        ds2401.write(0x33);
        for (i = 0; i < 8; i++)
            Temp_byte[i] = ds2401.read();

        if (OneWire::crc8(Temp_byte, 8) == 0)
        {
            for (i=1; i<7; i++)
                MAC_ID[i + 1] = Temp_byte[i];
        }

        else { MAC_ID[3] = 0xff; }
    }
    else { MAC_ID[3] = 0xaa; } //Nothing is connected in the bus
}

void Sensors_Setup(void)      // sensor initialization
{
#ifdef TMP112_include
    TMP112_CONFIG();
#endif

#ifdef  BMP180_include
    bmp.begin();
#endif

#ifdef MMA8452Q_include
    MMA8452_CONFIG(); //Test and intialize the MMA8452
#endif

#ifdef TSYS01_include
    TSYS01_CONFIG();
#endif

#ifdef TSL260RD_include
    mcp3428_1.init(MCP342X::L, MCP342X::L);
    mcp3428_2.init(MCP342X::L, MCP342X::F);
#endif

#ifdef HMC5883L_include
    HMC5883_Magnetometer.begin();
#endif
    return;
}


void writeEEPROM (unsigned int memory_address, byte data_byte )
{
    Wire.beginTransmission(EEPROM_ADDRESS);
    Wire.write((int)(memory_address >> 8));   // MSB
    Wire.write((int)(memory_address & 0xFF)); // LSB
    Wire.write(data_byte);
    Wire.endTransmission();
    delay(5);
}

byte readEEPROM (unsigned int memory_address )
{
    byte recv_data = 0xff;

    Wire.beginTransmission(EEPROM_ADDRESS);
    Wire.write((int)(memory_address >> 8));   // MSB
    Wire.write((int)(memory_address & 0xFF)); // LSB
    Wire.endTransmission();
    Wire.requestFrom(EEPROM_ADDRESS,1);

    if (Wire.available())
        recv_data = Wire.read();

    return recv_data;
}