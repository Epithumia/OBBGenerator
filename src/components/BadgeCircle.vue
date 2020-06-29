<template>
    <g>
        <g id="outer" :transform="'rotate('+outerRotation+' 200 200)'">
            <g id="inner" :transform="'rotate('+innerRotation+' 200 200)'">
                <circle stroke="#000000" clip-path="url(#cut-off-bottom)" id="circle2" cy="200px" stroke-width="0"
                        fill="url(#palette1)" r="200px" cx="200px" transform=""></circle>
                <circle stroke="#000000" clip-path="url(#cut-off-top)" id="circle3" cy="200px" stroke-width="0"
                        fill="url(#palette2)" r="200px" cx="200px" transform=""></circle>
            </g>
            <circle stroke="#000000" id="circle1" cy="200px" stroke-width="0" fill="url(#grad1)"
                    r="170px" cx="200px" transform=""></circle>
        </g>
        <path d="M50 10 m0.0 0-1.2837 2.6011-2.8705 0.41711 2.0771 2.0247-0.49033 2.8589 2.5674-1.3498 2.5674 1.3498-0.49034-2.8589 2.0771-2.0247-2.8705-0.41711z"
              fill="url(#palette3)" transform="scale(4)"></path>
        <path stroke="none" visibility="visible" id="universite-path" stroke-width="5" d="M8,200 A1,1 0 0 0 392,200"
              fill="none"></path>
        <path stroke="none" visibility="visible" id="skill-path" stroke-width="5" d="M22,200 A1,1 0 0 1 378,200"
              fill="none"></path>
        <text stroke="none" font-family="Open Sans" id="universite-text" stroke-width="1px"
              text-rendering="geometricPrecision" fill="url(#palette1)" font-size="26px" text-anchor="middle">
            <textPath href="#universite-path" startOffset="50%">{{univText}}</textPath>
        </text>
        <text stroke="none" font-family="Open Sans" id="skill-text" stroke-width="1px" alignment-baseline="central"
              text-rendering="geometricPrecision" fill="url(#palette2)" font-size="26px" text-anchor="middle">
            <textPath href="#skill-path" startOffset="50%">{{skillText}}</textPath>
        </text>
    </g>
</template>

<script>
    export default {
        props: {
            innerRotation: {
                type: Number,
                default: 0
            },
            outerRotation: {
                type: Number,
                default: 0
            },
            skillText: {
                type: String,
                default: ''
            },
            univText: {
                type: String,
                default: ''
            }
        }
    }
</script>
