<template>
    <div class="container">
        <div class="row justify-content-center">
            <div :class="selected ? 'col-md-8 mx-auto' : 'col-md-12'">
                <div id="openbbadgeSVG" v-if="selected">
                    <badge-base :uuid="params.uuid" :base-color="baseColor"
                                :secondary-color="secondaryColor"
                                :is-random="params.randomize">
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
                        <badge-base :uuid="params.uuid"
                                    :base-color="baseColor"
                                    :secondary-color="secondaryColor"
                                    :is-random="params.randomize">
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
            <div class="col-md-2"></div>
            <div class="col-md-4">
                <b-input-group size="sm">
                    <b-input-group-prepend>
                        <b-input-group-text style="width: 140px">
                            Couleur de base
                        </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-input type="color" v-model="params.xBaseColor"></b-form-input>
                    <b-form-input type="text" v-model="params.xBaseColor" class="col-md-3"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-4">
                <b-input-group size="sm">
                    <b-input-group-prepend>
                        <b-input-group-text style="width: 140px">
                            Couleur secondaire
                        </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-input type="color" v-model="params.xSecondaryColor"></b-form-input>
                    <b-form-input type="text" v-model="params.xSecondaryColor" class="col-md-3"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-2"></div>
        </div>
        <div class="row justify-content-center" v-if="!params.randomize">
            <div class="col-md-2"></div>
            <div class="col-md-4">
                <b-input-group size="sm">
                    <b-input-group-prepend>
                        <b-input-group-text style="width: 140px">
                            Année de début
                        </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-input type="text" v-model="params.anneeDebut"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-4">
                <b-input-group size="sm">
                    <b-input-group-prepend>
                        <b-input-group-text style="width: 140px">
                            Année de fin
                        </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-input type="text" v-model="params.anneeFin"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-2"></div>
        </div>
        <div class="row justify-content-center" v-if="!params.randomize">
            <div class="col-md-2"></div>
            <div class="col-md-4">
                <b-input-group size="sm">
                    <b-input-group-prepend>
                        <b-input-group-text style="width: 140px">
                            Emetteur
                        </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-input type="text" v-model="params.univText" class="col-md-12"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-4">
                <b-input-group size="sm">
                    <b-input-group-prepend>
                        <b-input-group-text style="width: 140px">
                            Catégorie
                        </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-input type="text" v-model="params.skillText" class="col-md-12"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-2"></div>
        </div>
        <div class="row justify-content-center" v-if="!params.randomize">
            <div class="col-md-2"></div>
            <div class="col-md-4">
                <b-input-group size="sm">
                    <b-input-group-prepend>
                        <b-input-group-text style="width: 140px">
                            Corps badge 1
                        </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-input type="text" v-model="params.texteBadge1" class="col-md-12"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-4">
                <b-input-group size="sm">
                    <b-input-group-prepend>
                        <b-input-group-text style="width: 140px">
                            Corps badge 2
                        </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-input type="text" v-model="params.texteBadge2" class="col-md-12"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-2"></div>
        </div>
        <div class="row justify-content-center" v-if="!params.randomize">
            <div class="col-md-2"></div>
            <div class="col-md-4">
                <b-input-group size="sm">
                    <b-input-group-prepend>
                        <b-input-group-text style="width: 140px">
                            Corps badge 3
                        </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-input type="text" v-model="params.texteBadge3" class="col-md-12"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-4">
                <b-input-group size="sm">
                    <b-input-group-prepend>
                        <b-input-group-text style="width: 140px">
                            Titre
                        </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-input type="text" v-model="params.cartoucheTitreBadge" class="col-md-12"></b-form-input>
                </b-input-group>
            </div>
            <div class="col-md-2"></div>
        </div>
        <div class="row justify-content-center" v-if="!params.randomize">
            <div class="col-md-2"></div>
            <div class="col-md-4">
                <b-input-group size="sm">
                    <b-input-group-prepend>
                        <b-input-group-text style="width: 140px">
                            Style de l'icone
                        </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-select v-model="selectedType" :options="optionsTypes"></b-form-select>
                </b-input-group>
            </div>
            <div class="col-md-4">
                <b-input-group size="sm">
                    <b-input-group-prepend>
                        <b-input-group-text style="width: 140px">
                            Icone du badge
                        </b-input-group-text>
                    </b-input-group-prepend>
                    <b-form-select v-model="selectedIcon" :options="optionsIcons"></b-form-select>
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
                    {value: 'hexa', text: 'Hexagone (WIP)'},
                    {value: 'cercle', text: 'Cercle (WIP)'}
                ],
                params: {
                    randomize: true,
                    xBaseColor: "#04B053",
                    xSecondaryColor: "#b00449",
                    innerRotation: 0,
                    outerRotation: 0,
                    univText: "Université de Montcuq",
                    skillText: "Pédagogie",
                    cartoucheTitreBadge: "CONTINUATEUR-TRICE",
                    anneeDebut: 2019,
                    anneeFin: 2020,
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
            },
            randomColor: function () {
                let r = Math.round(this.rng() * 255).toString()
                let g = Math.round(this.rng() * 255).toString()
                let b = Math.round(this.rng() * 255).toString()
                return Color('rgb(' + r + ',' + g + ',' + b + ')').hex()
            }
        },
        computed: {
            rng: function () {
                return seedrandom(this.params.uuid + '\0')
            },
            baseColor: function () {
                if (this.params.randomize) {
                    return this.randomColor()
                }
                return this.params.xBaseColor
            },
            secondaryColor: function () {
                if (this.params.randomize) {
                    return this.randomColor()
                }
                return this.params.xSecondaryColor
            },
            iconPath: function () {
                if (this.params.randomize) {
                    let keys = Object.keys(icons) // Types possibles
                    let nb = keys.length          // Nb de types
                    //let rng = seedrandom(this.params.uuid)
                    let n = Math.min(Math.round(this.rng() * nb), nb - 1) // Tirage au sort
                    let key = keys[n] // Type tiré au sort
                    let icon_list = icons[key]
                    let icon_keys = Object.keys(icon_list)
                    let icon_key = Math.min(Math.round(this.rng() * icon_keys.length), icon_keys.length - 1)
                    let icon = icon_list[icon_keys[icon_key]]
                    return window.location.href + icon.path
                }
                if (!this.selectedType) return ''
                if (!this.selectedIcon || !(this.selectedIcon in icons[this.selectedType])) return ''
                return window.location.href + icons[this.selectedType][this.selectedIcon].path
            },
            optionsIcons: function () {
                if (!this.selectedType) return []
                let opts = []
                let icon_list = icons[this.selectedType]
                for (let key of Object.keys(icon_list)) {
                    opts.push({value: key, text: icon_list[key].name})
                }
                console.log(opts)
                opts.sort((a, b) => (a.text.localeCompare(b.text)))
                return opts
            },
            optionsTypes: function () {
                let opts = []
                for (let t of Object.keys(icons)) {
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
                }
            },
            selectedType: {
                // getter
                get: function () {
                    if (!this.selectType && this.optionsTypes.length > 0) return this.optionsTypes[0].value
                    return this.selectType
                },
                // setter
                set: function (newValue) {
                    this.selectType = newValue
                    if (this.selectType && !this.selectIcon && this.optionsIcons.length > 0) return this.optionsIcons[0].value
                }
            }
        }
    }
</script>


