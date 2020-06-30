<template>
    <div class="container">
        <div class="row justify-content-center">
            <div :class="selected ? 'col-md-8 mx-auto' : 'col-md-12'">
                <div id="openbbadgeSVG" v-if="selected">
                    <badge-base :uuid="params.uuid" :base-color="baseColor" :is-random="params.randomize">
                        <badge-circle v-if="selected==='cercle'"
                                      :params="params"
                        />
                        <badge-hexa v-if="selected==='hexa'"
                                    :params="params"
                        />
                        <badge-hexa-dane v-if="selected==='hexadane'"
                                         :params="params"
                                         :icon-path="iconPath"
                        />
                    </badge-base>
                </div>
                <div v-else style="display: flex">
                    <div>
                        <badge-base :uuid="params.uuid" :base-color="baseColor" :is-random="params.randomize">
                            <badge-hexa-dane :params="params"
                                             :icon-path="iconPath"
                            />
                        </badge-base>
                        Hexagone (DANE)
                    </div>
                    <div>
                        <badge-base :uuid="params.uuid" :base-color="baseColor" :is-random="params.randomize">
                            <badge-hexa :params="params"
                            />
                        </badge-base>
                        Hexagone
                    </div>
                    <div>
                        <badge-base :uuid="params.uuid" :base-color="baseColor" :is-random="params.randomize">
                            <badge-circle :params="params"
                            />
                        </badge-base>
                        Cercle
                    </div>
                </div>
                <a href="#" @click="downloadSVG" class="link-download btn btn-primary btn-sm" v-if="selected">
                    Télécharger (SVG)
                </a>
            </div>
        </div>
        <div class="row justify-content-center mt-3">
            <div class="col-md-8 mx-auto">
                <b-input-group prepend="Aléatoire ?" append="Clé unique">
                    <b-input-group-prepend is-text>
                        <b-form-checkbox
                                switch
                                aria-label="Checkbox for following text input"
                                v-model="params.randomize">
                        </b-form-checkbox>
                    </b-input-group-prepend>
                    <b-form-input type="text" v-model="params.uuid" :disabled="!params.randomize"></b-form-input>
                </b-input-group>
                <b-input-group prepend="Type de badge">
                    <b-form-select v-model="selected" :options="options"></b-form-select>
                </b-input-group>
            </div>
        </div>
        <div class="row justify-content-center mt-3" v-if="!params.randomize">
            <div class="col-md-8 mx-auto">
                <b-input-group prepend="Couleur de base" size="sm">
                <b-form-input type="color" v-model="params.xBaseColor" class="col-md-2"></b-form-input>
                    <b-input-group-append>
                        <b-form-input type="text" v-model="params.xBaseColor" class="col-md-5"  size="sm"></b-form-input>
                    </b-input-group-append>
                </b-input-group>
            </div>
        </div>
        <div class="row justify-content-center" v-if="!params.randomize">
            <div class="col-md-2"></div>
            <div class="col-md-4">
                <b-input-group prepend="Année de début" size="sm">
                    <b-form-input type="text" v-model="params.anneeDebut" class="col-md-3"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-4">
                <b-input-group prepend="Année de fin" size="sm">
                    <b-form-input type="text" v-model="params.anneeFin" class="col-md-3"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-2"></div>
        </div>
        <div class="row justify-content-center" v-if="!params.randomize">
            <div class="col-md-2"></div>
            <div class="col-md-4">
                <b-input-group prepend="Emetteur" size="sm">
                    <b-form-input type="text" v-model="params.univText" class="col-md-12"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-4">
                <b-input-group prepend="Catégorie" size="sm">
                    <b-form-input type="text" v-model="params.skillText" class="col-md-12"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-2"></div>
        </div>
        <div class="row justify-content-center" v-if="!params.randomize">
            <div class="col-md-2"></div>
            <div class="col-md-4">
                <b-input-group prepend="Corps badge 1" size="sm">
                    <b-form-input type="text" v-model="params.texteBadge1" class="col-md-12"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-4">
                <b-input-group prepend="Corps badge 2" size="sm">
                    <b-form-input type="text" v-model="params.texteBadge2" class="col-md-12"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-2"></div>
        </div>
        <div class="row justify-content-center" v-if="!params.randomize">
            <div class="col-md-2"></div>
            <div class="col-md-4">
                <b-input-group prepend="Corps badge 3" size="sm">
                    <b-form-input type="text" v-model="params.texteBadge3" class="col-md-12"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-4">
                <b-input-group prepend="Titre" size="sm">
                    <b-form-input type="text" v-model="params.cartoucheTitreBadge" class="col-md-12"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-2"></div>
        </div>
        <div class="row justify-content-center" v-if="!params.randomize">
            <div class="col-md-2"></div>
            <div class="col-md-4">
                <b-input-group prepend="Icone du badge" size="sm">
                    <b-form-select v-model="selectedIcon" :options="optionsIcons"></b-form-select>
                </b-input-group>
            </div>
            <div class="col-md-4">
                <b-input-group prepend="Style de l'icone" size="sm">
                    <b-form-select v-model="selectedType" :options="optionsTypes"></b-form-select>
                </b-input-group>
            </div>
            <div class="col-md-2"></div>
        </div>
    </div>
</template>

<script>
    import BadgeBase from './BadgeBase.vue'
    import BadgeCircle from "@/components/BadgeCircle";
    import BadgeHexa from "@/components/BadgeHexa";
    import BadgeHexaDane from "@/components/BadgeHexaDane";
    import {uuid as UUID} from 'vue-uuid';

    const seedrandom = require('seedrandom');
    const Color = require('color');
    import icons from '@/assets/icon_list.json'

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
                params: {
                    randomize: true,
                    xBaseColor: "#04B053",
                    innerRotation: 0,
                    outerRotation: 0,
                    univText: "Université de Montcuq",
                    skillText: "Pédagogie",
                    cartoucheTitreBadge: "CONTINUATEUR-TRICE",
                    anneeDebut: 2019,
                    anneeFin:2020,
                    texteBadge1: "AGILITÉ",
                    texteBadge2: "PÉDADOGIQUE",
                    texteBadge3: "COVID-19",
                    iconPath: null,
                    uuid: UUID.v1()
                },
                selectIcon: null,
                selectType: null
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
                if (this.params.randomize) {
                    let rng = seedrandom(this.params.uuid)
                    let r = Math.round(rng() * 255).toString()
                    let g = Math.round(rng() * 255).toString()
                    let b = Math.round(rng() * 255).toString()
                    return Color('rgb(' + r + ',' + g + ',' + b + ')').hex()
                }
                return this.params.xBaseColor
            },
            iconPath: function () {
                if (this.params.randomize) {
                    let keys = Object.keys(icons)
                    let nb = keys.length
                    let rng = seedrandom(this.params.uuid)
                    let n = Math.min(Math.round(rng() * nb), nb - 1)
                    let key = keys[n]
                    let itypes = Object.keys(icons[key].types)
                    let nt = Math.min(Math.round(rng() * itypes.length), itypes.length - 1)
                    let t = icons[key]['types'][itypes[nt]]
                    return window.location.href+t.path
                }
                if (!this.selectedIcon) return ''
                if (!this.selectedType) return ''
                return window.location.href+icons[this.selectedIcon].types[this.selectedType].path
            },
            optionsIcons: function () {
                let opts = []
                for (let key of Object.keys(icons)){
                    opts.push({value: key, text: icons[key].name})
                }
                return opts
            },
            optionsTypes: function () {
                if (!this.selectedIcon) return []
                let icon = icons[this.selectedIcon]
                let opts = []
                for (let t of Object.keys(icon.types)) {
                    opts.push({value: t, text: t})
                }
                return opts
            },
            selectedIcon: {
                // getter
                get: function () {
                    if (!this.selectIcon && this.optionsIcons.length > 0) return this.optionsIcons[0].value
                    return this.selectIcon
                },
                // setter
                set: function (newValue) {
                    this.selectIcon = newValue
                    if (this.selectIcon && !this.selectType && this.optionsTypes.length > 0) this.selectedType = this.optionsTypes[0].value
                }
            },
            selectedType: {
                // getter
                get: function () {
                    if (this.selectedIcon && !this.selectType && this.optionsTypes.length > 0) return this.optionsTypes[0].value
                    return this.selectType
                },
                // setter
                set: function (newValue) {
                    this.selectType = newValue
                }
            }
        }
    }
</script>


