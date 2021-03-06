/* eslint no-console: 0 */
'use strict';

import React, { Component } from 'react';
import {
    AppRegistry,
    StyleSheet,
    Text,
    TextInput,
    View,
    DeviceEventEmitter  //react-native-sensor-manager
} from 'react-native';

// Sensor manager
// var sensorManager = require("NativeModules").SensorManager;
import { SensorManager } from 'NativeModules';

export default class masApp extends Component {
    constructor(props) {
        super(props);
        watchID: (null: ?number);  //FIXME: is this necesary?
        this.state = {
            lat: 0,
            lon: 0,
            speed: 0,
            accuracy: 0,
            altitude: 0,
            altitudeAccuracy: 0,
            heading: 0,

            x: 0,
            y: 0,
            z: 0,

            xg: 0,
            yg: 0,
            zg: 0,

            azimuth: 0, // Yaw
            pitch: 0,
            roll: 0,

            steps: 0,

            activity: "Unknown"
        };
    }

    componentDidMount() {
        this.watchID = navigator.geolocation.watchPosition((position) => {
                var lon = position.coords.longitude;
                var lat = position.coords.latitude;
                var speed = position.coords.speed;
                var accuracy = position.coords.accuracy;
                var altitude = position.coords.altitude;
                // var altitudeAccuracy = position.coords.altitudeAccuracy;
                var heading = position.coords.heading;

                this.setState({
                    lat: lat,
                    lon: lon,
                    speed: speed,
                    accuracy: accuracy,
                    altitude: altitude,
                    // altitudeAccuracy: altitudeAccuracy,
                    heading: heading
                });
                this.fetchGeolocation(lat,lon,speed,accuracy,altitude,heading,this.state.activity);
            },
            (error) => alert(JSON.stringify(error)),
            {enableHighAccuracy: true, timeout: 0, maximumAge: 1000, distanceFilter:4}
        );

        SensorManager.startAccelerometer(300); // Start the accelerometer with a minimum delay of 300 ms between events
        DeviceEventEmitter.addListener("Accelerometer", function (data) {
            var x = data.x;
            var y = data.y;
            var z = data.z;


            this.setState({
                x: x,
                y: y,
                z: z
            });
            this.fetchAccelerometer(this.state.x, this.state.y, this.state.z, this.state.activity);
        }.bind(this));

    }

    fetchGeolocation(lat, lon, speed, accuracy, altitude, heading, activity) {

        var URL = "http://138.68.86.63/storeGNSS?lat=" + lat + "&lon=" + lon + "&speed=" + speed +
            "&accuracy=" + accuracy + "&altitude=" + altitude +  "&heading=" + heading + "&activity=" + activity;

        fetch(URL)
        // TODO: don't actually need a response
            .then((response) => response.json())
            .then((responseData) => {
            })
            .catch((error) => {
                console.log("Something wrong with fetch gnss");
            })
            .done();
    }

    fetchAccelerometer(x, y, z, activity) {


        var URL = "http://138.68.86.63/storeACCELEROMETER?&x=" + x + "&y=" + y +
            "&z=" + z + "&activity=" + activity;

        fetch(URL)
        // TODO: don't actually need a response
            .then((response) => response.json())
            .then((responseData) => {
            })
            .catch((error) => {
                console.log("Something wrong with fetch accelerometer");
            })
            .done();
    }

    textInput = (text) => {
        this.setState((state) =>{
            return {
                activity: text

            };
        });
    };

    render(){
        return (
            <View>
              <Text>
                <Text style={styles.title}>Lat: </Text> {this.state.lat} <Text>{'\n'}</Text>
                <Text style={styles.title}>Lon: </Text> {this.state.lon} <Text>{'\n'}</Text>
                <Text style={styles.title}>Speed: </Text> {this.state.speed} <Text>{'\n'}</Text>
                <Text style={styles.title}>Accuracy: </Text> {this.state.accuracy} <Text>{'\n'}</Text>
                <Text style={styles.title}>Altitude: </Text> {this.state.altitude} <Text>{'\n'}</Text>
                <Text style={styles.title}>X: </Text> {this.state.x} <Text>{'\n'}</Text>
                <Text style={styles.title}>Y: </Text> {this.state.y} <Text>{'\n'}</Text>
                <Text style={styles.title}>Z: </Text> {this.state.z} <Text>{'\n'}</Text>
                <Text style={styles.title}>Activity: </Text> {this.state.activity} <Text>{'\n'}</Text>
              </Text>
            <TextInput

                style={{height: 40, borderColor: 'gray', borderWidth: 1}}
                onSubmitEditing={(activity) => this.textInput(activity.nativeEvent.text)}
            />
            </View>
        )
    }
}
const styles = StyleSheet.create({
    title: {
        fontWeight: '500',
    },
});

AppRegistry.registerComponent('masApp', () => masApp);
