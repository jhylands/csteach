<?php
$classArray = array('map','playerDuck');
genClasses($classArray);

function genClasses($classes){
	for ($class in $classes){
		$myfile = fopen($class['name'] . ".java", "w") or die("Unable to open file!");
		fwrite($myfile, genClass($class['name'],$class['inherits'],$class['functions']));
		fclose($myfile);
	}
	return true;
}


function genClass($className,$inherits,$functions){
	$functionCode = genFunctions($functions);
	$classcode = <<<code
package ducky;
public class $className $inherits {
$functionCode
}
code;
	return $classcode;
}

function genFunctions($functions){
	$functionCode = "";
	for ($function in $functions){
		$functionCode .= genFunction($function['name'],$function['type']);
	}
	return $functionCode;
}

function genFunction($name,$type,$public ,$static){
	$functionCode= <<<code
$public $static $type function $name(){
//code
	return null;
	}
code;
	return $functionCode;
}
?>
