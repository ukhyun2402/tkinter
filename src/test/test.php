<?php
$hlfields = get_field_objects( 22 );
foreach ( $hlfields as ['name' => $name, 'value' => $value] ) {

    $cb = function() use ($name) {
        $field = get_field($name, 22);
        return $field;
    };  
    add_shortcode( $name, $cb );
}