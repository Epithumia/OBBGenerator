<template>
    <svg xmlns="http://www.w3.org/2000/svg"
         :width="scaledWidth"
         :height="scaledHeight"
         viewBox="0 0 400 400"
         :aria-labelledby="iconName"
         role="presentation"
    >
        <defs>
            <clipPath id="cut-off-bottom">
                <rect x="0" y="0" width="400" height="200" stroke-width="3" stroke="red" fill="blue"
                      transform="" id="rect1"></rect>
            </clipPath>
            <clipPath id="cut-off-top">
                <rect x="0" y="200" width="400" height="200" stroke-width="3" stroke="red" fill="blue"
                      transform="" id="rect2"></rect>
            </clipPath>
            <linearGradient id="grad1" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" :style="'stop-color:'+color5+';stop-opacity:1'"/>
                <stop offset="100%" :style="'stop-color:'+color4+';stop-opacity:1'"/>
            </linearGradient>
            <linearGradient id="palette1">
                <stop offset="0%" :stop-color="color1"/>
                <stop offset="100%" :stop-color="color1"/>
            </linearGradient>
            <linearGradient id="palette2">
                <stop offset="0" :stop-color="color2"/>
            </linearGradient>
            <linearGradient id="palette3">
                <stop offset="0%" :stop-color="color3"/>
                <stop offset="100%" :stop-color="color3"/>
            </linearGradient>
            <linearGradient id="palette4">
                <stop offset="0" :stop-color="color4"/>
            </linearGradient>
            <linearGradient id="palette5">
                <stop offset="0" :stop-color="color5"/>
            </linearGradient>
            <component :is="'style'" id="Open Sans_Google_Webfont_import">
                @import url(https://fonts.googleapis.com/css?family=Open+Sans);
            </component>
        </defs>
        <slot></slot>
        <title :id="iconName" lang="fr">
            {{ iconName }} Badge
        </title>
    </svg>
</template>

<script>
    var Color = require('color');

    export default {
        props: {
            iconName: {
                type: String,
                default: 'OB'
            },
            width: {
                type: [Number, String],
                default: 200
            },
            height: {
                type: [Number, String],
                default: 200
            },
            scale: {
                type: Number,
                default: 2
            },
            gradStart: {
                type: String,
                default: "#FFFF00"
            },
            gradEnd: {
                type: String,
                default: "#FF0000"
            },
            baseColor: {
                type: String,
                default: "#000000"
            },
            secondaryColor: {
                type: String,
                default: "#ffffff"
            }
        },
        computed: {
            color1: function(){
                return this.baseColor
            },
            color2: function () {
                return this.lightenBy(Color(this.color1), 0.5).hex()
            },
            color3: function () {
                return this.lightenBy(Color(this.color1), 0.75).hex()
            },
            color4: function () {
                return this.secondaryColor
            },
            color5: function () {
                return this.lightenBy(Color(this.color4), 0.5).hex()
            },
            scaledWidth: function () {
                return Math.round(this.width * this.scale)
            },
            scaledHeight: function () {
                return Math.round(this.height * this.scale)
            }
        },
        methods: {
            colorLuminance: function (hex, lum) {

                // validate hex string
                hex = String(hex).replace(/[^0-9a-f]/gi, '');
                if (hex.length < 6) {
                    hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2];
                }
                lum = lum || 0;

                // convert to decimal and change luminosity
                var rgb = "#", c, i;
                for (i = 0; i < 3; i++) {
                    c = parseInt(hex.substr(i * 2, 2), 16);
                    c = Math.round(Math.min(Math.max(0, c + (c * lum)), 255)).toString(16);
                    rgb += ("00" + c).substr(c.length);
                }

                return rgb;
            },
            lightenBy: function (color, ratio) {
                const lightness = color.lightness();
                return color.lightness(lightness + (100 - lightness) * ratio);
            },
            darkenBy: function (color, ratio) {
                const lightness = color.lightness();
                return color.lightness(lightness - lightness * ratio);
            }
        }
    }
</script>
