import * as openapi from "openapi-typescript";
const openapiTS =  openapi.default;

export default function say(string_to_say) {
    return console.log(string_to_say);
};