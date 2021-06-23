import * as openapi from "openapi-typescript";
const openapiTS =  openapi.default;



/* creating a global library sdk that could be use by app developer around the world to work with tight coupling */

export const ChooseModels = function (schemas : string[]) {
    return console.log(schemas);
};

export const SyncModel = function (template : string) {
    return console.log(template);
};

export default function Create(template : string) {
    return console.log(template);
};