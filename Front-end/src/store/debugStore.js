import { reactive } from "vue";

export const debugStore = reactive({
    enabled: false,
    debug: null,

    toggle() {
        this.enabled = !this.enabled;
    },

    setDebug(data) {
        this.debug = data;
    }
});
