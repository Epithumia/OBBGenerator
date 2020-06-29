<template>
    <div class="container">
        <div class="row justify-content-center">
            <div :class="selected ? 'col-md-6 mx-auto' : 'col-md-12'">
                <div id="openbbadgeSVG" v-if="selected">
                    <badge-base :uuid="uuid" :base-color="baseColor" :is-random="randomize">
                        <badge-circle v-if="selected==='cercle'"
                                      :inner-rotation="innerRotation"
                                      :outer-rotation="outerRotation"
                                      :univ-text="univText"
                                      :skill-text="skillText"
                        />
                        <badge-hexa v-if="selected==='hexa'"
                                    :inner-rotation="innerRotation"
                                    :outer-rotation="outerRotation"
                                    :univ-text="univText"
                                    :skill-text="skillText"
                        />
                        <badge-hexa-dane v-if="selected==='hexadane'"
                                         :inner-rotation="innerRotation"
                                         :outer-rotation="outerRotation"
                                         :univ-text="univText"
                                         :skill-text="skillText"
                        />
                    </badge-base>
                </div>
                <div v-else style="display: flex">
                    <badge-base :uuid="uuid" :base-color="baseColor" :is-random="randomize">
                        <badge-hexa-dane :inner-rotation="innerRotation"
                                         :outer-rotation="outerRotation"
                                         :univ-text="univText"
                                         :skill-text="skillText"
                        />
                    </badge-base>
                    <badge-base :uuid="uuid" :base-color="baseColor" :is-random="randomize">
                        <badge-hexa :inner-rotation="innerRotation"
                                    :outer-rotation="outerRotation"
                                    :univ-text="univText"
                                    :skill-text="skillText"
                        />
                    </badge-base>
                    <badge-base :uuid="uuid" :base-color="baseColor" :is-random="randomize">
                        <badge-circle :inner-rotation="innerRotation"
                                      :outer-rotation="outerRotation"
                                      :univ-text="univText"
                                      :skill-text="skillText"
                        />
                    </badge-base>
                </div>
                <p>
                    OBBadge ({{uuid}} : {{baseColor}})
                </p>
                <a href="#" @click="downloadSVG" class="link-download btn btn-primary btn-sm" v-if="selected">
                    Télécharger (SVG)
                </a>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-md-6 mx-auto">
                <b-form-select v-model="selected" :options="options"></b-form-select>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-md-3"></div>
            <div class="col-md-4 mx-auto">
                <b-form-input type="color" v-model="xBaseColor"></b-form-input>
            </div>
            <div class="col-md-2 mx-auto">
                {{xBaseColor}}
            </div>
            <div class="col-md-3"></div>
        </div>
        <div class="row justify-content-center">
            <div class="col-md-3"></div>
            <div class="col-md-4 mx-auto">
                <b-form-input type="text" v-model="uuid"></b-form-input>
            </div>
            <div class="col-md-2 mx-auto">
                <b-form-checkbox v-model="randomize">Aléatoire ?</b-form-checkbox>
            </div>
            <div class="col-md-3"></div>
        </div>
    </div>
</template>

<script>
    import BadgeBase from './BadgeBase.vue'
    import BadgeCircle from "@/components/BadgeCircle";
    import BadgeHexa from "@/components/BadgeHexa";
    import BadgeHexaDane from "@/components/BadgeHexaDane";
    import {uuid as UUID} from 'vue-uuid';

    var seedrandom = require('seedrandom');
    var Color = require('color');

    export default {
        components: {
            BadgeHexaDane,
            BadgeCircle,
            BadgeHexa,
            BadgeBase
        },
        data() {
            return {
                selected: null,
                options: [
                    {value: null, text: 'Choisir une forme de base'},
                    {value: 'hexadane', text: 'Hexagone (DANE)'},
                    {value: 'hexa', text: 'Hexagone'},
                    {value: 'cercle', text: 'Cercle'}
                ],
                randomize: true,
                xBaseColor: "#113248",
                innerRotation: 0,
                outerRotation: 0,
                univText: "Université de Montcuq",
                skillText: "Pédagogie",
                uuid: UUID.v1()
            }
        },
        methods: {
            downloadSVG: function (evt) {
                const svgContent = document.getElementById("openbbadgeSVG").innerHTML,
                    blob = new Blob([svgContent], {
                        type: "image/svg+xml"
                    }),
                    url = window.URL.createObjectURL(blob),
                    link = evt.target;
                link.target = "_blank";
                link.download = "Illustration1.svg";
                link.href = url;
            }
        },
        computed: {
            baseColor: function () {
                if (this.randomize) {
                    let rng = seedrandom(this.uuid)
                    let r = Math.round(rng() * 255).toString()
                    let g = Math.round(rng() * 255).toString()
                    let b = Math.round(rng() * 255).toString()
                    return Color('rgb(' + r + ',' + g + ',' + b + ')').hex()
                }
                return this.xBaseColor
            }
        }
    }
</script>


