<template>
    <div>
        <icon-base><icon-circle /></icon-base>
        <p>
            You can use whatever icon you want and keep the base consistent with slots
        </p>
        <select></select>
    </div>
</template>

<script>
    import IconBase from './IconBase.vue'
    import IconCircle from "@/components/IconCircle";

    export default {
        components: {
            IconCircle,
            IconBase
        }
    }
</script>


